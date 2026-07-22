FROM public.ecr.aws/lambda/python:3.13

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy ALL application files
COPY *.py ./

# Lambda Handler
CMD ["lambda_function.lambda_handler"]
