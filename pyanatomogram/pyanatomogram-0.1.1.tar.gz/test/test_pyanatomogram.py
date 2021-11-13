import io
import os
import pathlib
import random
import tempfile
import unittest

import matplotlib.pyplot
import pandas
import seaborn

import pyanatomogram


def compare_to_golden_file(test, result, golden_filename):
    golden_filename = pathlib.Path(golden_filename)
    try:
        golden = golden_filename.read_text()
        test.assertEqual(golden, result)
    except (AssertionError, FileNotFoundError) as exc:
        with tempfile.NamedTemporaryFile(
            "w", suffix=golden_filename.suffix, delete=False
        ) as tmpfile:
            tmpfile.write(result)
            raise AssertionError(
                "Did not match golden file {}. Results saved in {}".format(
                    golden_filename, tmpfile.name
                )
            ) from exc


class TestGallusGallus(unittest.TestCase):
    def setUp(self):
        # Set reproducible hash for saving svg files.
        matplotlib.rcParams["svg.hashsalt"] = "TEST"
        os.environ["SOURCE_DATE_EPOCH"] = "0"

    def test_get_tissue_names(self):
        anatomogram = pyanatomogram.Anatomogram("gallus_gallus")
        self.assertListEqual(
            [
                "brain",
                "heart",
                "kidney",
                "liver",
                "skeletal muscle organ",
                "colon",
                "spleen",
                "lung",
            ],
            anatomogram.get_tissue_names(),
        )

    def test_to_svg(self):
        anatomogram = pyanatomogram.Anatomogram("gallus_gallus")
        compare_to_golden_file(self, anatomogram.to_svg(), "golden_gallus_gallus.svg")

    def test_set_tissue_style(self):
        anatomogram = pyanatomogram.Anatomogram("gallus_gallus")
        anatomogram.set_tissue_style("heart", fill="red")
        compare_to_golden_file(
            self, anatomogram.to_svg(), "golden_gallus_gallus_red_heart.svg"
        )

    def test_highlight_tissues(self):
        anatomogram = pyanatomogram.Anatomogram("gallus_gallus")
        anatomogram.highlight_tissues({"brain": 1, "heart": 3, "colon": 7}, cmap="Reds")
        compare_to_golden_file(
            self, anatomogram.to_svg(), "golden_gallus_gallus_highlighted_tissues.svg"
        )

    def test_matplotlib_export(self):
        fig, ax = matplotlib.pyplot.subplots(nrows=1, ncols=2)
        anatomogram = pyanatomogram.Anatomogram("gallus_gallus")
        anatomogram.highlight_tissues({"brain": 1, "heart": 3, "colon": 7}, cmap="Reds")
        anatomogram.to_matplotlib(ax[0])
        anatomogram = pyanatomogram.Anatomogram("gallus_gallus")
        anatomogram.highlight_tissues({"brain": 7, "heart": 1, "colon": 3}, cmap="Reds")
        anatomogram.to_matplotlib(ax[1])
        f = io.StringIO()
        fig.savefig(f, format="svg")
        compare_to_golden_file(
            self, f.getvalue(), "golden_gallus_gallus_matplotlib_figure.svg"
        )

    def test_facetgrid_helper(self):
        df = pandas.DataFrame.from_records(
            [
                ["a", "brain", 1],
                ["a", "heart", 10],
                ["b", "heart", 5],
                ["b", "colon", 2],
            ],
            columns=["group", "organ", "value"],
        )
        norm = matplotlib.colors.Normalize(vmin=0, vmax=10)
        g = seaborn.FacetGrid(df, col="group")
        g.map(
            pyanatomogram.facetgrid_helper,
            "organ",
            "value",
            name="gallus_gallus",
            norm=norm,
            cmap="Reds",
        )
        f = io.StringIO()
        g.fig.savefig(f, format="svg")
        compare_to_golden_file(
            self, f.getvalue(), "golden_gallus_gallus_facetgrid_helper.svg"
        )


class TestHomoSapiens(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        os.environ["SOURCE_DATE_EPOCH"] = "0"

    def test_get_tissue_names(self):
        anatomogram = pyanatomogram.Anatomogram("homo_sapiens.male")
        self.assertListEqual(
            [
                "cerebral cortex",
                "pleura",
                "brain",
                "heart",
                "breast",
                "thyroid gland",
                "adrenal gland",
                "lymph node",
                "bone marrow",
                "adipose tissue",
                "skeletal muscle",
                "leukocyte",
                "frontal cortex",
                "temporal lobe",
                "prefrontal cortex",
                "pituitary gland",
                "atrial appendage",
                "aorta",
                "coronary artery",
                "gastroesophageal junction",
                "left ventricle",
                "hippocampus",
                "caecum",
                "ileum",
                "rectum",
                "nose",
                "tongue",
                "left atrium",
                "pulmonary valve",
                "mitral valve",
                "penis",
                "vas deferens",
                "seminal vesicle",
                "testis",
                "epididymis",
                "eye",
                "nasal septum",
                "oral cavity",
                "tonsil",
                "nasal pharynx",
                "lung",
                "spinal cord",
                "amygdala",
                "trachea",
                "throat",
                "bronchus",
                "tricuspid valve",
                "diaphragm",
                "liver",
                "stomach",
                "spleen",
                "duodenum",
                "gall bladder",
                "pancreas",
                "colon",
                "small intestine",
                "appendix",
                "smooth muscle",
                "urinary bladder",
                "prostate gland",
                "nerve",
                "cerebellum",
                "cerebellar hemisphere",
                "kidney",
                "renal cortex",
                "bone",
                "cartilage",
                "esophagus",
                "salivary gland",
                "parotid gland",
                "submandibular gland",
                "skin",
            ],
            anatomogram.get_tissue_names(),
        )

    def test_highlight_all_tissues(self):
        anatomogram = pyanatomogram.Anatomogram("homo_sapiens.male")
        tissues = anatomogram.get_tissue_names()
        random.shuffle(tissues)  # Avoid similar colors for neighbouring tissues.
        anatomogram.highlight_tissues(
            {tissue: i for i, tissue in enumerate(tissues)}, cmap="jet"
        )
        compare_to_golden_file(
            self,
            anatomogram.to_svg(),
            "golden_homo_sapiens.male_highlighted_all_tissues.svg",
        )


if __name__ == "__main__":
    unittest.main()
