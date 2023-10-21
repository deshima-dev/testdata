# standard library
from pathlib import Path


# dependencies
from decode import io
from pytest import mark


# constants
DEMS_DIR = Path(__file__).parents[1] / "dems"
DEMS_ALL = map(Path, DEMS_DIR.glob("*.nc.gz"))


# test functions
@mark.parametrize("dems", DEMS_ALL)
def test_open(dems: Path) -> None:
    """Test existence and opening of DEMS."""
    io.open_dems(dems)
