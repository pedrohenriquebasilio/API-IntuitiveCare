from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="API de Busca de Operadoras de Saúde",
    description="API para buscar operadoras de saúde a partir de um CSV",
    version="1.0.0"
)
class SearchRequest(BaseModel):
    query: str
    limit: Optional[int] = 10
@app.on_event("startup")
async def load_data():
    global operadoras_df
    operadoras_df = pd.read_csv("Relatorio_cadop.csv", sep=";", encoding="utf-8")
    operadoras_df = operadoras_df.fillna("")
    def calculate_relevance(row, query):
    score = 0
    query_lower = query.lower()
    
    for field in ["Razao_Social", "Nome_Fantasia", "Cidade", "UF"]:
        if query_lower in str(row[field]).lower():
            score += 1
            
            if str(row[field]).lower().startswith(query_lower):
                score += 2
    return score
@app.post("/search", response_model=List[dict])
async def search_operadoras(request: SearchRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query não pode estar vazia")

    operadoras_df["relevance"] = operadoras_df.apply(
        lambda row: calculate_relevance(row, request.query), axis=1
    )
    resultados = (
        operadoras_df[operadoras_df["relevance"] > 0]
        .sort_values(by="relevance", ascending=False)
        .head(request.limit)
        .drop(columns=["relevance"])
        .to_dict(orient="records")
    )

    if not resultados:
        return []
    
    return resultados

#Rota de verificacao
@app.get("/")
async def root():
    return {"message": "API de Busca de Operadoras de Saúde está funcionando!"}