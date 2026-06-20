import pandas as pd


def main():

    try:

        expected = pd.read_csv(
            "dataset/sample_claims.csv"
        )

        predicted = pd.read_csv(
            "output.csv"
        )

        print(
            "Expected rows:",
            len(expected)
        )

        print(
            "Predicted rows:",
            len(predicted)
        )

        if len(predicted) == 0:

            print(
                "\nERROR: output.csv is empty"
            )

            return

        # Align row counts
        min_rows = min(
            len(expected),
            len(predicted)
        )

        expected = expected.iloc[
            :min_rows
        ].reset_index(
            drop=True
        )

        predicted = predicted.iloc[
            :min_rows
        ].reset_index(
            drop=True
        )

        print(
            "\nComparing",
            min_rows,
            "rows..."
        )

        metrics = [
            "claim_status",
            "issue_type",
            "object_part",
            "severity"
        ]

        print("\nRESULTS")
        print("=" * 40)

        for column in metrics:

            if (
                column in expected.columns
                and
                column in predicted.columns
            ):

                correct = (
                    expected[column]
                    .astype(str)
                    .str.lower()
                    ==
                    predicted[column]
                    .astype(str)
                    .str.lower()
                ).sum()

                accuracy = round(
                    correct
                    /
                    min_rows
                    * 100,
                    2
                )

                print(
                    f"{column}: "
                    f"{correct}/{min_rows} "
                    f"({accuracy}%)"
                )

        print("\nEvaluation Complete")

    except FileNotFoundError as e:

        print(
            "File not found:",
            e
        )

    except Exception as e:

        print(
            "Evaluation error:",
            e
        )


if __name__ == "__main__":
    main()