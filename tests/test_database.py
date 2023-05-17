import json
import tempfile

import pytest

from my_lib.database import process_database


def test_process_database():
    # Non existing file
    with pytest.raises(FileNotFoundError):
        process_database("./imaginary_file.json")

    dummy_payload = {"Hello": "world"}
    with tempfile.NamedTemporaryFile() as tmp_file:
        with open(str(tmp_file), "w") as f:
            json.dump(dummy_payload, f)

        assert isinstance(process_database(str(tmp_file)), dict)
