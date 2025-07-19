from pathlib import Path
from analyzer.strength_checker import analyze_strength
from analyzer.breach_checker import is_password_breach  # Assuming it returns count or None

def batch_password_checker(filepath: str, output_report: str = "audit_report.txt") -> str:
    filepath = Path(filepath)
    extension = filepath.suffix.lower()
    if extension != ".txt":
        return "Currently only .txt files are supported."

    if not filepath.exists():
        return "File does not exist."

    lines = filepath.read_text().splitlines()
    report_lines = []
    report_lines.append("\n Batch Password Audit Results:\n" + "-" * 40)

    for idx, line in enumerate(lines, start=1):
        password = line.strip()
        if not password:
            continue

        strength_result = analyze_strength(password)
        breach_count = is_password_breach(password)

        report_lines.append(f"\n🔐 Password {idx}: {password}")
        report_lines.append(f"Strength  : {strength_result['strength']}")

        if breach_count:
            report_lines.append(f"Breach status  : Found in {breach_count} breaches")
        else:
            report_lines.append("Breach status  : Not found in known breaches")

        report_lines.append("-" * 40)

    # Save report to file
    report_path = Path(output_report)
    report_path.write_text("\n".join(report_lines))

    return f"\n✅ Batch password checking completed. Report saved to: {report_path}"
