FROM agrigorev/zoomcamp-model:2025

WORKDIR /code

# Copy project files
COPY pyproject.toml uv.lock ./
# If you don't have uv.lock, you can rely on pip: uncomment below
# RUN pip install fastapi uvicorn scikit-learn==1.6.1

# If using uv and lockfile:
RUN pip install uv && uv sync --frozen

ENV PATH="/code/.venv/bin:$PATH"


# Copy app and the pipeline (use v1 or v2 file required)
COPY app.py pipeline_v1.bin ./

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9696"]
