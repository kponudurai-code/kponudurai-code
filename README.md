Polatis project

Run tests with coverage using the project's virtual environment:

```powershell
# From repository root
.
.venv\Scripts\Activate.ps1  # if using PowerShell
python -m pytest --cov=libraries --cov-report=term-missing --cov-report=html:reports/coverage_html
```

HTML reports:
- Test HTML report: `reports/report.html`
- Coverage HTML: `reports/coverage_html/index.html`
