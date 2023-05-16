# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

import json
import os
from typing import Any, Dict, List

__all__ = ["process_database"]


def process_database(file_path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(file_path):
        raise FileNotFoundError

    with open(file_path, "rb") as f:
        db = json.load(f)

    return db
