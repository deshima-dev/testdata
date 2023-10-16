# standard library
from pathlib import Path


# dependencies
import xarray as xr
from pytest import mark


# constants
DEMS_DIR = Path(__file__).parents[1] / "dems"
DEMS_ALL = list(DEMS_DIR.glob("*.nc.gz"))


# test functions
@mark.parametrize("dems", DEMS_ALL)
def test_open(dems: Path) -> None:
    """Test existence and opening of DEMSs."""
    xr.open_dataarray(dems)
