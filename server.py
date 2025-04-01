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