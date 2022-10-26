poetry install
echo '\n\033[1;33mStatic Type Checking\033[0m'
poetry run pyright

echo '\n\033[1;33mLint w/ Black\033[0m'
poetry run black --check --verbose .

echo '\n\033[1;33mExercise 1 Tests\033[0m';
poetry run python -m unittest -v tests.tests || python3 -m unittest -v ..tests.tests