from typing import Type

import pytest

from pikepdf import Array, Dictionary, Name, Page, Pdf, Rectangle

# pylint: disable=redefined-outer-name


@pytest.fixture
def graph(resources):
    yield Pdf.open(resources / 'graph.pdf')


@pytest.fixture
def fourpages(resources):
    yield Pdf.open(resources / 'fourpages.pdf')


@pytest.fixture
def graph_page(graph):
    return graph.pages[0]


def test_page_boxes(graph_page):
    page = graph_page
    assert page.mediabox == page.cropbox == page.trimbox
    page.cropbox = [0, 0, page.mediabox[2] - 100, page.mediabox[3] - 100]
    page.mediabox = [
        page.mediabox[0] - 50,
        page.mediabox[1] - 50,
        page.mediabox[2] + 50,
        page.mediabox[3] + 50,
    ]
    page.trimbox = [50, 50, page.mediabox[2] - 50, page.mediabox[3] - 50]

    assert page.mediabox != page.cropbox
    assert page.cropbox != page.mediabox

    page.cropbox = Array([0, 0, 50, 50])


def test_invalid_boxes(graph_page):
    page = graph_page
    with pytest.raises(ValueError):
        page.mediabox = 'hi'
    with pytest.raises(ValueError):
        page.mediabox = [0, 0, 0]
    with pytest.raises(ValueError):
        page.mediabox = [0, 0, 0, 0, 0, 0]


def test_page_repr(graph_page):
    r = repr(graph_page)
    assert r.startswith('<pikepdf.Page')
    assert '(Type="/Page")' not in r


class TestAddResource:
    d = Dictionary(Type=Name.XObject, Subtype=Name.Image, Width=1, Height=1)

    def test_basic(self, graph_page):
        d = self.d

        with pytest.raises(ValueError, match="already exists"):
            graph_page.add_resource(d, Name.XObject, Name.Im0, replace_existing=False)

        res = graph_page.add_resource(d, Name.XObject, Name.Im0, replace_existing=True)
        assert graph_page.resources.XObject[res].Width == 1

        res2 = graph_page.add_resource(d, Name.XObject, prefix='Im')
        assert str(res2).startswith("/Im")
        assert graph_page.resources.XObject[res2].Height == 1

    def test_resources_exists_but_wrong_type(self, graph_page):
        del graph_page.obj.Resources
        graph_page.obj.Resources = Name.Dummy
        with pytest.raises(TypeError, match='exists but is not a dictionary'):
            graph_page.add_resource(
                self.d, Name.XObject, Name.Im0, replace_existing=False
            )

    def test_create_resource_dict_if_not_exists(self, graph_page):
        del graph_page.obj.Resources
        graph_page.add_resource(self.d, Name.XObject, Name.Im0, replace_existing=False)
        assert Name.Resources in graph_page.obj

    def test_name_and_prefix(self, graph_page):
        with pytest.raises(ValueError, match="one of"):
            graph_page.add_resource(self.d, Name.XObject, name=Name.X, prefix='y')

    def test_unrecognized_object_not_disturbed(self, graph_page):
        graph_page.obj.Resources.InvalidItem = Array([42])
        graph_page.add_resource(self.d, Name.Pattern)
        assert Name.InvalidItem in graph_page.obj.Resources


def test_add_unowned_page():  # issue 174
    pdf = Pdf.new()
    d = Dictionary(Type=Name.Page)
    pdf.pages.append(d)


def test_failed_add_page_cleanup():
    pdf = Pdf.new()
    d = Dictionary(Type=Name.NotAPage)
    num_objects = len(pdf.objects)
    with pytest.raises(TypeError, match="only pages can be inserted"):
        pdf.pages.append(d)
    assert len(pdf.pages) == 0

    # If we fail to add a new page, we expect one new null object handle to be
    # be added (since QPDF does not remove the object outright)
    assert len(pdf.objects) == num_objects + 1, "QPDF semantics changed"
    assert pdf.objects[-1] is None, "Left a stale object behind without deleting"

    # But we'd better not delete an existing object...
    d2 = pdf.make_indirect(Dictionary(Type=Name.StillNotAPage))
    with pytest.raises(TypeError, match="only pages can be inserted"):
        pdf.pages.append(d2)
    assert len(pdf.pages) == 0

    assert d2.same_owner_as(pdf.Root)


def test_formx(graph, outpdf):
    formx = graph.pages[0].as_form_xobject()
    graph.add_blank_page()
    new_page = graph.pages[-1]
    formx_placed_name = new_page.add_resource(formx, Name.XObject)
    cs = new_page.calc_form_xobject_placement(
        formx, formx_placed_name, Rectangle(0, 0, 200, 200)
    )
    assert bytes(formx_placed_name) in cs
    new_page.obj.Contents = graph.make_stream(cs)
    graph.save(outpdf)


def test_fourpages_to_4up(fourpages, graph, outpdf):
    pdf = Pdf.new()
    pdf.add_blank_page(page_size=(1000, 1000))
    page = pdf.pages[0]

    pdf.pages.extend(fourpages.pages)

    # Keep explicit Page(pdf.pages[..]) here
    page.add_overlay(pdf.pages[1], Rectangle(0, 500, 500, 1000))
    page.add_overlay(Page(pdf.pages[2]), Rectangle(500, 500, 1000, 1000))
    page.add_overlay(Page(pdf.pages[3]).as_form_xobject(), Rectangle(0, 0, 500, 500))
    page.add_underlay(pdf.pages[4], Rectangle(500, 0, 1000, 500))

    page.add_underlay(graph.pages[0])

    with pytest.raises(TypeError):
        page.add_overlay(Dictionary(Key=123))

    del pdf.pages[1:]

    pdf.save(outpdf)


def test_push_stack(fourpages, outpdf):
    pdf = Pdf.new()
    pdf.add_blank_page(page_size=(1000, 1000))
    page = pdf.pages[0]

    pdf.pages.extend(fourpages.pages)

    page.Contents = pdf.make_stream(
        b"0.4 G\n"
        b"0 500 500 1000 re s\n"
        b"500 500 1000 1000 re s\n"
        b"-1 0 0 1 500 0 cm\n"
    )

    page.add_overlay(pdf.pages[1], Rectangle(0, 500, 500, 1000), push_stack=False)
    page.add_overlay(pdf.pages[2], Rectangle(500, 500, 1000, 1000), push_stack=True)

    # Test requires visual confirmation
    # Second page should be in upper right corner, properly positioned for a 4-up
    # First page should be mirrored horizontally since stack was not pushed

    del pdf.pages[1:]
    pdf.save(outpdf)


def test_cant_hash_page(graph):
    with pytest.raises(TypeError, match="mutable"):
        hash(graph.pages[0])


def test_contents_add(graph):
    graph.pages[0].contents_add(b'q Q', prepend=True)

    new_cs = graph.make_stream(b'q Q')
    graph.pages[0].contents_add(new_cs, prepend=False)

    graph.pages[0].contents_coalesce()
    assert graph.pages[0].Contents.read_bytes().startswith(b'q Q')
    assert graph.pages[0].Contents.read_bytes().endswith(b'q Q')


def test_page_attrs(graph):
    # Test __getattr__
    assert isinstance(graph.pages[0].Resources, Dictionary)

    del graph.pages[0].Resources
    with pytest.raises(AttributeError, match="can't delete"):
        del graph.pages[0].obj
    del graph.pages[0]['/Contents']

    assert Name.Contents not in graph.pages[0] and Name.Resources not in graph.pages[0]
