"""ImmApp: Immediate App Toolkit for ImGui Bundle
"""
# ruff: noqa: B008, F821
from typing import Tuple, Optional, Callable, List, overload, Any
import enum

from imgui_bundle import imgui_md, hello_imgui, ImVec2
from imgui_bundle.imgui_node_editor import (
    Config as NodeEditorConfig,
    EditorContext as NodeEditorContext,
)
from imgui_bundle.hello_imgui import DefaultWindowSize

ImGuiMd = imgui_md
HelloImGui = hello_imgui

VoidFunction = Callable[[], Any]
ScreenSize = Tuple[int, int]
DefaultScreenSize = (800, 600)

# fmt: off

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:immapp.h>    ####################
####################    </generated_from:immapp.h>    ####################


####################    <generated_from:runner.h>    ####################
class AddOnsParams:
    """///////////////////////////////////////////////////////////////////////////////////////

     AddOnParams: require specific ImGuiBundle packages (markdown, node editor, texture viewer)
     to be initialized at startup.

    /////////////////////////////////////////////////////////////////////////////////////
    """

    # Set withImplot=True if you need to plot graphs
    with_implot: bool = False

    # Set withMarkdown=True if you need to render Markdown
    # (alternatively, you can set withMarkdownOptions)
    with_markdown: bool = False

    # Set withNodeEditor=True if you need to render a node editor
    # (alternatively, you can set withNodeEditorConfig)
    with_node_editor: bool = False

    # Set withTexInspect=True if you need to use imgui_tex_inspect
    with_tex_inspect: bool = False

    # You can tweak NodeEditorConfig (but this is optional)
    with_node_editor_config: Optional[NodeEditorConfig] = None

    # You can tweak MarkdownOptions (but this is optional)
    with_markdown_options: Optional[ImGuiMd.MarkdownOptions] = None
    def __init__(
        self,
        with_implot: bool = False,
        with_markdown: bool = False,
        with_node_editor: bool = False,
        with_tex_inspect: bool = False,
        with_node_editor_config: Optional[NodeEditorConfig] = None,
        with_markdown_options: Optional[ImGuiMd.MarkdownOptions] = None,
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

# ///////////////////////////////////////////////////////////////////////////////////////
#
# Helpers to run an app from C++
#
# /////////////////////////////////////////////////////////////////////////////////////
# Run an application using HelloImGui params + some addons
@overload
def run(
    runner_params: HelloImGui.RunnerParams,
    add_ons_params: AddOnsParams = AddOnsParams(),
) -> None:
    pass

@overload
def run(
    simple_params: HelloImGui.SimpleRunnerParams,
    add_ons_params: AddOnsParams = AddOnsParams(),
) -> None:
    pass

@overload
def run(
    gui_function: VoidFunction,
    window_title: str = "",
    window_size_auto: bool = False,
    window_restore_previous_geometry: bool = False,
    window_size: ScreenSize = DefaultWindowSize,
    fps_idle: float = 10.0,
    with_implot: bool = False,
    with_markdown: bool = False,
    with_node_editor: bool = False,
    with_tex_inspect: bool = False,
    with_node_editor_config: Optional[NodeEditorConfig] = None,
    with_markdown_options: Optional[ImGuiMd.MarkdownOptions] = None,
) -> None:
    """///////////////////////////////////////////////////////////////////////////////////////

     Helpers to run an app from Python (using named parameters)

    /////////////////////////////////////////////////////////////////////////////////////
     Helper to run an app inside imgui_bundle, using HelloImGui:

     (HelloImGui::SimpleRunnerParams)
         - `guiFunction`: the function that will render the ImGui widgets
         - `windowTitle`: title of the window
         - `windowSizeAuto`: if True, autosize the window from its inner widgets
         - `windowRestorePreviousGeometry`: if True, restore window size and position from last run
         - `windowSize`: size of the window
         - `fpsIdle`: fps of the application when idle

     (ImmApp::AddOnsParams)
         - `with_implot`: if True, then a context for implot will be created/destroyed automatically
         - `with_markdown` / `with_markdown_options`: if specified, then  the markdown context will be initialized
           (i.e. required fonts will be loaded)
         - `with_node_editor` / `with_node_editor_config`: if specified, then a context for imgui_node_editor
           will be created automatically.
    """
    pass

def run_with_markdown(
    gui_function: VoidFunction,
    window_title: str = "",
    window_size_auto: bool = False,
    window_restore_previous_geometry: bool = False,
    window_size: ScreenSize = DefaultWindowSize,
    fps_idle: float = 10.0,
    with_implot: bool = False,
    with_node_editor: bool = False,
    with_tex_inspect: bool = False,
    with_node_editor_config: Optional[NodeEditorConfig] = None,
    with_markdown_options: Optional[ImGuiMd.MarkdownOptions] = None,
) -> None:
    """Run an application with markdown"""
    pass

# ///////////////////////////////////////////////////////////////////////////////////////
#
# Dpi aware utilities (which call the same utilities from HelloImGui)
#
# /////////////////////////////////////////////////////////////////////////////////////

@overload
def em_size() -> float:
    """EmSize() returns the visible font size on the screen. For good results on HighDPI screens, always scale your
    widgets and windows relatively to this size.
    It is somewhat comparable to the [em CSS Unit](https://lyty.dev/css/css-unit.html).
    EmSize() = ImGui::GetFontSize()
    """
    pass

@overload
def em_size(nb_lines: float) -> float:
    """EmSize(nbLines) returns a size corresponding to nbLines text lines"""
    pass

# EmToVec2() returns an ImVec2 that you can use to size or place your widgets in a DPI independent way
@overload
def em_to_vec2(x: float, y: float) -> ImVec2:
    pass

@overload
def em_to_vec2(v: ImVec2) -> ImVec2:
    pass

def default_node_editor_context() -> NodeEditorContext:
    """///////////////////////////////////////////////////////////////////////////////////////

     Utility for ImGui node editor

    /////////////////////////////////////////////////////////////////////////////////////
    """
    pass
####################    </generated_from:runner.h>    ####################


####################    <generated_from:clock.h>    ####################
def clock_seconds() -> float:
    """Chronometer in seconds"""
    pass
####################    </generated_from:clock.h>    ####################


####################    <generated_from:code_utils.h>    ####################
# <submodule code_utils>
class code_utils:  # Proxy class that introduces typings for the *submodule* code_utils
    pass  # (This corresponds to a C++ namespace. All method are static!)
    """ namespace CodeUtils"""

    @staticmethod
    def unindent(code: str, is_markdown: bool) -> str:
        pass
    @staticmethod
    def unindent_code(code: str) -> str:
        pass
    @staticmethod
    def unindent_markdown(code: str) -> str:
        pass

# </submodule code_utils>
####################    </generated_from:code_utils.h>    ####################


####################    <generated_from:snippets.h>    ####################
# <submodule snippets>
class snippets:  # Proxy class that introduces typings for the *submodule* snippets
    pass  # (This corresponds to a C++ namespace. All method are static!)
    #
    # TextEditorBundle: addition to ImGuiColorTextEdit, specific to ImGuiBundle
    #

    class SnippetLanguage(enum.Enum):
        cpp = enum.auto()  # (= 0)
        hlsl = enum.auto()  # (= 1)
        glsl = enum.auto()  # (= 2)
        c = enum.auto()  # (= 3)
        sql = enum.auto()  # (= 4)
        angel_script = enum.auto()  # (= 5)
        lua = enum.auto()  # (= 6)
        python = enum.auto()  # (= 7)

    class SnippetTheme(enum.Enum):
        dark = enum.auto()  # (= 0)
        light = enum.auto()  # (= 1)
        retro_blue = enum.auto()  # (= 2)
        mariana = enum.auto()  # (= 3)
    @staticmethod
    def default_snippet_language() -> SnippetLanguage:
        """DefaultSnippetLanguage will be Cpp or Python if using python bindings."""
        pass

    class SnippetData:
        code: str = ""
        language: SnippetLanguage = DefaultSnippetLanguage()
        palette: SnippetTheme = SnippetTheme.light

        show_copy_button: bool = (
            True  # Displayed on top of the editor (Top Right corner)
        )
        show_cursor_position: bool = True  # Show line and column number
        displayed_filename: str = ""  # Displayed on top of the editor

        height_in_lines: int = 0  # Number of visible lines in the editor
        max_height_in_lines: int = 40  # If the number of lines in the code exceeds this, the editor will scroll. Set to 0 to disable.

        read_only: bool = False  # Snippets are read-only by default

        border: bool = False  # Draw a border around the editor

        de_indent_code: bool = (
            True  # Keep the code indentation, but remove main indentation,
        )
        # so that the displayed code start at column 1
        def __init__(
            self,
            code: str = "",
            language: SnippetLanguage = DefaultSnippetLanguage(),
            palette: SnippetTheme = SnippetTheme.light,
            show_copy_button: bool = True,
            show_cursor_position: bool = True,
            displayed_filename: str = "",
            height_in_lines: int = 0,
            max_height_in_lines: int = 40,
            read_only: bool = False,
            border: bool = False,
            de_indent_code: bool = True,
        ) -> None:
            """Auto-generated default constructor with named params"""
            pass
    @staticmethod
    def show_code_snippet(
        snippet_data: SnippetData, width: float = 0.0, override_height_in_lines: int = 0
    ) -> None:
        pass
    @staticmethod
    @overload
    def show_side_by_side_snippets(
        snippet1: SnippetData,
        snippet2: SnippetData,
        hide_if_empty: bool = True,
        equal_visible_lines: bool = True,
    ) -> None:
        pass
    @staticmethod
    @overload
    def show_side_by_side_snippets(
        snippets: List[SnippetData],
        hide_if_empty: bool = True,
        equal_visible_lines: bool = True,
    ) -> None:
        pass

# </submodule snippets>
####################    </generated_from:snippets.h>    ####################

# </litgen_stub> // Autogenerated code end!
