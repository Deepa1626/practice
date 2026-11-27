from pathlib import Path

DATA_FILE = Path("employee.txt")


def load_employee(file_path: Path = DATA_FILE) -> dict[str, str]:
    """Read key-value employee details from employee.txt."""
    if not file_path.exists():
        return {}

    record: dict[str, str] = {}
    for line in file_path.read_text(encoding="utf-8").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            record[key.strip()] = value.strip()
    return record


def save_employee(record: dict[str, str], file_path: Path = DATA_FILE) -> None:
    """Write employee details back to employee.txt."""
    lines = [f"{key}: {value}" for key, value in record.items()]
    file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_role(new_role: str, file_path: Path = DATA_FILE) -> dict[str, str]:
    """Update the Role field and save to disk."""
    record = load_employee(file_path)
    record["Role"] = new_role
    save_employee(record, file_path)
    return record


if __name__ == "__main__":
    sample_record = {
        "Employee ID": "101",
        "Name": "Rahul",
        "Department": "Engineering",
        "Role": "Software Developer",
    }

    if not DATA_FILE.exists():
        save_employee(sample_record)

    current = load_employee()
    print("Current employee record:")
    for field, val in current.items():
        print(f"  {field}: {val}")
