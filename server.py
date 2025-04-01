from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="API de Busca de Operadoras de Saúde",
    description="API para buscar operadoras de saúde a partir de um CSV",
    version="1.0.0"
)