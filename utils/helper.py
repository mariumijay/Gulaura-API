import json
from typing import Any, Dict

def load_data(filepath: str) -> Dict[str, Any]:
    """Load JSON data from file"""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_data(filepath: str, data: Dict[str, Any]) -> None:
    """Save data to JSON file"""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def total_order_price(items: Dict[str, int], flowers_data: dict) -> float:
    """
    items: dict with flower_id as key and quantity as value
    flowers_data: dict loaded from flowers JSON
    """
    total = 0
    for flower_id, qty in items.items():
        flower_info = flowers_data.get(flower_id)
        if flower_info:
            total += flower_info["price"] * qty
    return total
