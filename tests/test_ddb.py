# standard library
from pathlib import Path


# dependencies
from astropy.io import fits
from pytest import mark


# constants
DDB_DIR = Path(__file__).parents[1] / "ddb"
DDB_ALL = list(DDB_DIR.glob("*.fits.gz"))


# test functions
@mark.parametrize("ddb", DDB_ALL)
def test_open(ddb: Path) -> None:
    """Test existence and opening of DDBs."""
    with fits.open(ddb):
        pass
