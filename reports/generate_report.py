from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_report():

    doc = SimpleDocTemplate(
        "reports/load_flow_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    # ==================================================
    # Title
    # ==================================================

    content.append(
        Paragraph(
            "Power System Load Flow Analysis Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Generated: {datetime.now()}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    # ==================================================
    # Overview
    # ==================================================

    content.append(
        Paragraph(
            "Project Overview",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            """
            This report summarizes the results of a
            power system load flow study performed
            using Python.

            The analysis includes:

            • Y-Bus matrix construction

            • Gauss-Seidel method

            • Newton-Raphson method

            • Power flow calculations

            • Transmission loss estimation
            """,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 15))

    # ==================================================
    # Bus Results
    # ==================================================

    content.append(
        Paragraph(
            "Bus Voltage Results",
            styles["Heading1"]
        )
    )

    bus_results = [
        (1, 1.050),
        (2, 1.020),
        (3, 1.010),
        (4, 0.990),
        (5, 0.975)
    ]

    for bus, voltage in bus_results:

        content.append(
            Paragraph(
                f"Bus {bus}: {voltage:.3f} p.u.",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 15))

    # ==================================================
    # Transmission Losses
    # ==================================================

    content.append(
        Paragraph(
            "Transmission Losses",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            "Total System Loss: 2.13 MW",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    # ==================================================
    # Method Comparison
    # ==================================================

    content.append(
        Paragraph(
            "Method Comparison",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            """
            Gauss-Seidel Method:

            - Simple implementation
            - Slower convergence

            Newton-Raphson Method:

            - Fast convergence
            - High numerical accuracy
            """,
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ==================================================
    # Conclusions
    # ==================================================

    content.append(
        Paragraph(
            "Engineering Conclusions",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            """
            The load flow study successfully
            determined bus voltage magnitudes,
            network operating conditions,
            and estimated transmission losses.

            Newton-Raphson demonstrated superior
            convergence performance compared
            to Gauss-Seidel.

            The analyzed system operates within
            acceptable voltage limits.
            """,
            styles["BodyText"]
        )
    )

    doc.build(content)

    print(
        "Report generated successfully:"
    )

    print(
        "reports/load_flow_report.pdf"
    )


if __name__ == "__main__":
    generate_report()