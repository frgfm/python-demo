# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

import json
import os
from typing import Any, Dict, List

__all__ = ["load_annotations"]


def load_annotations(data_path: str, file_filter: List[str]) -> Dict[str, Dict[str, Any]]:
    """Converts temperatures from Fahrenheit to Celsius.

    Args:
        input_temperatures: the list of temperatures in Fahrenheit

    Returns:
        the temperatures converted to Celsius
    """

    if not os.path.exists(data_path):
    	raise FileNotFoundError

    with open(data_path, "rb") as f:
    	annotations = json.load(data_path)

    return {file: annotations[file] for file in file_filter}