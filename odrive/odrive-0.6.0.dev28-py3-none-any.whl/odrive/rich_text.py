
class RichText():
    STYLE_DEFAULT = object()
    STYLE_GREEN = object()
    STYLE_YELLOW = object()
    STYLE_GRAY = object()
    STYLE_RED = object()
    STYLE_BOLD = object()

    def __init__(self, val, style = None):
        """
        val: A string, a RichText object or a list of strings or RichText
        objects.
        style: If specified, overrides the style of all segments in `val`.
        If not specified, uncolored strings are set to the default color.
        """

        if not (isinstance(val, tuple) or isinstance(val, list)):
            val = [val]

        self.segments = []
        for segment in val:
            if isinstance(segment, str):
                self.segments.append((segment, style or RichText.STYLE_DEFAULT))
            elif isinstance(segment, RichText):
                self.segments += segment.segments
            else:
                raise Exception("unsupported argument")
        
        if not style is None:
            self.segments = [(''.join([s[0] for s in self.segments]), style)]

    def __add__(self, other):
        if isinstance(other, str) or isinstance(other, RichText):
            return RichText([self, other])
        else:
            raise NotImplementedError()

    def __radd__(self, other):
        if isinstance(other, str) or isinstance(other, RichText):
            return RichText([other, self])
        else:
            raise NotImplementedError()
    
    def __repr__(self):
        return ''.join([s[0] for s in self.segments])

    def join(self, others):
        segments = []
        for item in others:
            segments.append(self)
            segments.append(item)
        return RichText(segments[1:]) if len(segments) > 0 else RichText("")
