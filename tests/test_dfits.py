# standard library
from pathlib import Path


# dependencies
from astropy.io import fits
from pytest import mark


# constants
DFITS_DIR = Path(__file__).parents[1] / "dfits"
DFITS_ALL = list(DFITS_DIR.glob("*.fits.gz"))


# test functions
@mark.parametrize("dfits", DFITS_ALL)
def test_open(dfits: Path) -> None:
    """Test existence and opening of DFITSs."""
    with fits.open(dfits):
        pass
