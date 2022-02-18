import matplotlib as mpl
mpl.use('agg')
from matplotlib.testing.compare import compare_images
from tempfile import NamedTemporaryFile
import os.path
import pygenometracks.plotTracks

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "test_data")

browser_tracks_with_hic = """
[hic]
file = Li_et_al_2015.h5

[hic_matrix_square]
file = Li_et_al_2015.h5
title = no region2 on h5 file
file_type = hic_matrix_square

[hic_matrix_square2]
file = Li_et_al_2015.cool
region2 = X:3000000-3500000
title = region2 = X:3000000-3500000 on cool file
file_type = hic_matrix_square

[hic_matrix_square3]
file = Li_et_al_2015.h5
region2 = chrX:3000000-3500000
title = region2 = chrX:3000000-3500000 on h5 file forced height
height = 2
file_type = hic_matrix_square

[hic_matrix_square4]
file = Li_et_al_2015.cool
transform = log1p
show_masked_bins = true
orientation = inverted
title = cool file log1p show_masked_bins inverted
file_type = hic_matrix_square

[hic_matrix_square5]
file = Li_et_al_2015.cool
transform = log
title = cool file log max_value = 2
max_value = 2
file_type = hic_matrix_square

[x-axis]
"""

with open(os.path.join(ROOT, "hic_square.ini"), 'w') as fh:
    fh.write(browser_tracks_with_hic)

browser_tracks_with_hic = """
[hic matrix]
file = small_test3.cool
title = cool with few interactions transform = no hic_matrix_square
file_type = hic_matrix_square
min_value = 0
max_value = 50

[hic matrix]
file = small_test3.cool
title = cool with few interactions transform = -log hic_matrix_square
transform = -log
file_type = hic_matrix_square
min_value = 0
max_value = -5
"""

with open(os.path.join(ROOT, "browser_tracks_hic_small_test_square.ini"), 'w') as fh:
    fh.write(browser_tracks_with_hic)

browser_tracks_with_hic = """
[hic matrix]
file = small_test3.cool
title = cool with few interactions hic_matrix_square region2 = chr19:0-100000
region2 = chr19:0-100000
file_type = hic_matrix_square

[hic matrix]
file = small_test3.cool
title = cool with few interactions hic_matrix_square region2 = chr1:195400000-195600000
region2 = chr1:195400000-195600000
file_type = hic_matrix_square

[hic matrix]
file = small_test3.cool
title = cool with few interactions hic_matrix_square region2 = chr1:300000000-300200000
region2 = chr1:300000000-300200000
file_type = hic_matrix_square
"""

with open(os.path.join(ROOT, "browser_tracks_hic_small_test_square_bad_region2.ini"), 'w') as fh:
    fh.write(browser_tracks_with_hic)

tolerance = 13  # default matplotlib pixed difference tolerance


def test_hic_square():

    outfile = NamedTemporaryFile(suffix='.png', prefix='pyGenomeTracks_test_',
                                 delete=False)
    ini_file = os.path.join(ROOT, "hic_square.ini")
    region = "chrX:2500000-3500000"
    expected_file = os.path.join(ROOT, 'master_hic_square.png')
    args = f"--tracks {ini_file} --region {region} "\
           "--trackLabelFraction 0.23 --width 38 --dpi 130 "\
           f"--outFileName {outfile.name}".split()
    pygenometracks.plotTracks.main(args)
    res = compare_images(expected_file,
                         outfile.name, tolerance)
    assert res is None, res

    os.remove(outfile.name)


def test_hic_square_dec():

    outfile = NamedTemporaryFile(suffix='.png', prefix='pyGenomeTracks_test_',
                                 delete=False)
    ini_file = os.path.join(ROOT, "hic_square.ini")
    region = "X:2500000-3500000"
    expected_file = os.path.join(ROOT, 'master_hic_square_dec.png')
    args = f"--tracks {ini_file} --region {region} "\
           "--trackLabelFraction 0.23 --width 38 --dpi 130 "\
           "--decreasingXAxis "\
           f"--outFileName {outfile.name}".split()
    pygenometracks.plotTracks.main(args)
    res = compare_images(expected_file,
                         outfile.name, tolerance)
    assert res is None, res

    os.remove(outfile.name)


def test_plot_tracks_with_hic_small_square():
    outfile = NamedTemporaryFile(suffix='.png', prefix='pyGenomeTracks_test_',
                                 delete=False)
    ini_file = os.path.join(ROOT, 'browser_tracks_hic_small_test_square.ini')
    region = 'chr1:0-200000'
    expected_file = os.path.join(ROOT, 'master_hic_small_test_square.png')

    args = f"--tracks {ini_file} --region {region} "\
           "--trackLabelFraction 0.23 --width 38 --dpi 130 "\
           f"--outFileName {outfile.name}".split()
    pygenometracks.plotTracks.main(args)
    res = compare_images(expected_file,
                         outfile.name, tolerance)
    assert res is None, res

    os.remove(outfile.name)


def test_plot_tracks_with_hic_small_square_chrX():
    outfile = NamedTemporaryFile(suffix='.png', prefix='pyGenomeTracks_test_',
                                 delete=False)
    ini_file = os.path.join(ROOT, 'browser_tracks_hic_small_test_square.ini')
    region = 'chrX:0-200000'
    expected_file = os.path.join(ROOT, 'master_hic_small_test_square_chrX.png')

    args = f"--tracks {ini_file} --region {region} "\
           "--trackLabelFraction 0.23 --width 38 --dpi 130 "\
           f"--outFileName {outfile.name}".split()
    pygenometracks.plotTracks.main(args)
    res = compare_images(expected_file,
                         outfile.name, tolerance)
    assert res is None, res

    os.remove(outfile.name)


def test_plot_tracks_with_hic_small_square_invalid_region2():
    outfile = NamedTemporaryFile(suffix='.png', prefix='pyGenomeTracks_test_',
                                 delete=False)
    ini_file = os.path.join(ROOT, 'browser_tracks_hic_small_test_square_bad_region2.ini')
    for region in ['chr1:0-200000', 'chr19:0-200000', 'chr1:195400000-195600000', 'chr1:195600000-195800000']:
        expected_file = os.path.join(ROOT, 'master_hic_small_test_square_bad_region2.png')

        args = f"--tracks {ini_file} --region {region} "\
               "--trackLabelFraction 0.23 --width 38 --dpi 130 "\
               f"--outFileName {outfile.name}".split()
        pygenometracks.plotTracks.main(args)
        res = compare_images(expected_file,
                             outfile.name, tolerance)
        assert res is None, res

        os.remove(outfile.name)
