from __future__ import annotations

import imgui_bundle
from imgui_bundle.demos.demo_composition_graph.functions_composition_graph import AnyDataWithGui, FunctionWithGui
from imgui_bundle import immvision, imgui
from imgui_bundle import imgui_node_editor, implot, ImVec2

import numpy as np
from typing import List, Tuple, Optional
import cv2


Image = np.ndarray


def split_channels(image: Image) -> Image:
    assert len(image.shape) == 3
    depth_first = np.squeeze(np.dsplit(image, image.shape[-1]))
    return depth_first


class ImageWithGui(AnyDataWithGui):
    array: Image
    image_params: immvision.ImageParams

    def __init__(self, image: Image, zoom_key="z", image_display_width=200):
        self.array = image
        self.first_frame = True
        self.image_params = immvision.ImageParams()
        self.image_params.image_display_size = (image_display_width, 0)
        self.image_params.zoom_key = zoom_key

    def gui_data(self, function_name: str) -> None:
        self.image_params.refresh_image = self.first_frame
        _, self.image_params.image_display_size = gui_edit_size(self.image_params.image_display_size)
        immvision.image(function_name, self.array, self.image_params)
        self.first_frame = False
        if imgui.small_button("Inspect"):
            immvision.inspector_add_image(self.array, function_name)

    def gui_set_input(self) -> Optional[ImageWithGui]:
        from imgui_bundle import im_file_dialog as ifd

        if imgui.button("Select image file"):
            ifd.FileDialog.instance().open(
                "ImageOpenDialog",
                "Choose an image",
                "Image file (*.png*.jpg*.jpeg*.bmp*.tga).png,.jpg,.jpeg,.bmp,.tga,.*",
                False,
            )

        result = None
        imgui_node_editor.suspend_editor_canvas()
        if ifd.FileDialog.instance().is_done("ImageOpenDialog"):
            if ifd.FileDialog.instance().has_result():
                ifd_result = ifd.FileDialog.instance().get_result().path()
                image = cv2.imread(ifd_result)
                if image is not None:
                    result = ImageWithGui(image)
            ifd.FileDialog.instance().close()
        imgui_node_editor.resume_editor_canvas()

        return result


class ImagesWithGui(AnyDataWithGui):
    array: Image
    images_params: List[immvision.ImageParams]

    def __init__(
        self,
        images: Image,  # images is a numpy of several image along the first axis
        zoom_key="z",
        image_display_width=200,
        share_image_params: bool = False,
    ):
        self.array = images
        self.first_frame = True

        def make_image_params():
            image_params = immvision.ImageParams()
            image_params.image_display_size = (image_display_width, 0)
            image_params.zoom_key = zoom_key
            return image_params

        self.images_params = []
        if share_image_params:
            self.images_params.append(make_image_params())
        else:
            for i in range(len(images)):
                self.images_params.append(make_image_params())

    def gui_data(self, function_name: str) -> None:
        refresh_image = self.first_frame
        self.first_frame = False

        changed, self.images_params[0].image_display_size = gui_edit_size(self.images_params[0].image_display_size)
        if changed:
            for params in self.images_params:
                params.image_display_size = self.images_params[0].image_display_size

        for i, image in enumerate(self.array):
            image_params = self.images_params[i] if i < len(self.images_params) else self.images_params[0]
            image_params.refresh_image = refresh_image
            label = f"{function_name} - {i}"
            immvision.image(label, image, image_params)
            if imgui.small_button("Inspect"):
                immvision.inspector_add_image(image, label)


class SplitChannelsWithGui(FunctionWithGui):
    def f(self, x: AnyDataWithGui) -> ImagesWithGui:
        assert type(x) == ImageWithGui
        channels = split_channels(x.array)
        channels_normalized = channels / 255.0
        r = ImagesWithGui(channels_normalized)
        return r

    def name(self) -> str:
        return "SplitChannels"


class MergeChannelsWithGui(FunctionWithGui):
    def f(self, x: AnyDataWithGui) -> ImageWithGui:
        assert type(x) == ImagesWithGui
        channels = [c for c in x.array]
        image_float = np.dstack(channels)
        image_int = (image_float * 255.0).astype("uint8")
        r = ImageWithGui(image_int)
        return r

    def name(self) -> str:
        return "MergeChannels"


CvSize = Tuple[int, int]


def gui_edit_size(size: CvSize) -> Tuple[bool, CvSize]:
    def modify_size_by_ratio(ratio: float) -> CvSize:
        w = int(size[0] * ratio + 0.5)
        h = int(size[1] * ratio + 0.5)
        return w, h

    changed = False
    ratio = 1.05
    imgui.push_button_repeat(True)
    imgui.text("Thumbnail size")
    imgui.same_line()
    if imgui.small_button(" smaller "):
        size = modify_size_by_ratio(1.0 / ratio)
        changed = True
    imgui.same_line()
    if imgui.small_button(" bigger "):
        size = modify_size_by_ratio(ratio)
        changed = True
    imgui.pop_button_repeat()

    return changed, size


###############################################################################
#     LUT
###############################################################################

class LutImage:
    pow_exponent: float = 1

    _lut_graph: np.ndarray
    _lut_graph_needs_refresh: bool = True

    def apply(self, image: Image) -> Image:
        image_adjusted = np.power(image, self.pow_exponent)
        return image_adjusted

    def _show_lut_graph_opencv(self):
        if not hasattr(self, "_lut_graph"):
            self._prepare_lut_graph_opencv()
        immvision.image_display("Lut", self._lut_graph, refresh_image=self._lut_graph_needs_refresh)
        self._lut_graph_needs_refresh = False

    def _prepare_lut_graph_opencv(self):
        x = np.arange(0.0, 1.0, 1.0 / 255.0)
        y = np.power(x, self.pow_exponent)
        graph_size = int(imgui_bundle.em_size() * 2.)
        self._lut_graph = immvision._draw_lut_graph(list(x), list(y), (graph_size, graph_size))  # type: ignore
        self._lut_graph_needs_refresh = True

    def gui_params(self) -> bool:
        self._show_lut_graph_opencv()
        imgui.same_line()

        imgui.begin_group()
        imgui.text("Gamma power")
        imgui.set_next_item_width(100)
        changed, self.pow_exponent = imgui.slider_float(
            "##power", self.pow_exponent, 0.0, 10.0, flags=imgui.ImGuiSliderFlags_.logarithmic
        )
        if changed:
            self._prepare_lut_graph_opencv()
        imgui.end_group()
        return changed


class LutImageWithGui(FunctionWithGui):
    lut_image: LutImage

    def __init__(self):
        self.lut_image = LutImage()

    def f(self, x: AnyDataWithGui) -> ImageWithGui:
        assert type(x) == ImageWithGui

        image_adjusted = self.lut_image.apply(x.array)
        return ImageWithGui(image_adjusted)

    def name(self) -> str:
        return "LUT"

    def gui_params(self) -> bool:
        return self.lut_image.gui_params()


class LutChannelsWithGui(FunctionWithGui):
    channel_luts: List[LutImage]

    def __init__(self):
        self.channel_luts = []

    def add_params_on_demand(self, nb_channels: int):
        while len(self.channel_luts) < nb_channels:
            self.channel_luts.append(LutImage())

    def f(self, x: AnyDataWithGui) -> ImagesWithGui:
        assert type(x) == ImagesWithGui

        original_channels = x.array
        self.add_params_on_demand(len(original_channels))

        adjusted_channels = np.zeros_like(original_channels)
        for i in range(len(original_channels)):
            adjusted_channels[i] = self.channel_luts[i].apply(original_channels[i])

        r = ImagesWithGui(adjusted_channels)
        return r

    def name(self) -> str:
        return "LUT channels"

    def gui_params(self) -> bool:
        changed = False
        for i, channel_adjust_param in enumerate(self.channel_luts):
            imgui.push_id(i)
            changed |= channel_adjust_param.gui_params()
            imgui.pop_id()
        return changed