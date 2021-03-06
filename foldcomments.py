import sublime, sublime_plugin

# Do not load automatically:
#
# class FoldFileComments(sublime_plugin.EventListener):
#     def on_load(self, view):
#         for region in view.find_by_selector('comment'):
#             offset = view.find('#', region.a).b
#             view.fold(sublime.Region(offset, region.b - 1))

class ToggleCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view     = self.view
        comments = view.find_by_selector('comment')

        if view.fold(comments[0]):
            # first comment is unfolded. fold everything
            for region in view.find_by_selector('comment'):
                # do not single line comments
                is_multi_line = len(view.lines(region)) > 1
                is_long_line  = region.b - region.a > 80
                if is_multi_line or is_long_line:
                  offset = view.find('#', region.a).b
                  view.fold(sublime.Region(offset, region.b - 1))
        else:
            view.unfold(comments)

class FoldCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in view.find_by_selector('comment'):
            if len(view.lines(region)) > 1:
              offset = view.find('#', region.a).b
              view.fold(sublime.Region(offset, region.b - 1))

class UnfoldCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        view.unfold(view.find_by_selector('comment'))
