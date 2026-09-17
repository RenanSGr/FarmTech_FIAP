library(httr)
library(jsonlite)

cat("===================================================\n")
cat(" FARMTECH SOLUTIONS - MÓDULO R (ANÁLISE E CLIMA)\n")
cat("===================================================\n\n")

cat("[1] Buscando previsão do tempo via API (São Paulo)...\n")

url_api <- "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America%2FSao_Paulo"

resposta <- GET(url_api)

if (status_code(resposta) == 200) {
  dados_clima <- content(resposta, as = "parsed", type = "application/json")
  
  cat("\n--- PREVISÃO METEOROLÓGICA (Próximos 7 dias) ---\n")
  datas <- dados_clima$daily$time
  temp_max <- unlist(dados_clima$daily$temperature_2m_max)
  temp_min <- unlist(dados_clima$daily$temperature_2m_min)
  chuva <- unlist(dados_clima$daily$precipitation_sum)
  
  for (i in 1:length(datas)) {
    cat(sprintf("Data: %s | Temp: %.1f°C a %.1f°C | Chuva: %.1f mm\n", 
                datas[[i]], temp_min[i], temp_max[i], chuva[i]))
  }
} else {
  cat("Erro ao conectar na API de clima. Verifique sua conexão.\n")
}

cat("\n===================================================\n")

cat("\n[2] Processando dados das fazendas...\n")

if (file.exists("dados_farmtech.csv")) {
  
  df <- read.csv("dados_farmtech.csv", encoding = "UTF-8")
  
  insumos_cana <- df$quantidade_insumo[df$cultura == "Cana-de-açúcar"]
  insumos_laranja <- df$quantidade_insumo[df$cultura == "Laranja"]
  
  cat("\n--- ESTATÍSTICAS DE CONSUMO DE INSUMOS ---\n")
  
  if (length(insumos_cana) > 0) {
    cat("\n-> CULTURA: CANA-DE-AÇÚCAR (Fertilizante NPK)\n")
    cat(sprintf("Média de aplicação: %.2f kg\n", mean(insumos_cana)))
    
    if (length(insumos_cana) > 1) {
      cat(sprintf("Desvio Padrão: %.2f kg\n", sd(insumos_cana)))
    } else {
      cat("Desvio Padrão: N/A (Requer mais de 1 fazenda cadastrada)\n")
    }
  } else {
    cat("\n-> Nenhuma fazenda de Cana-de-açúcar cadastrada.\n")
  }
  
  if (length(insumos_laranja) > 0) {
    cat("\n-> CULTURA: LARANJA (Defensivo Foliar)\n")
    cat(sprintf("Média de aplicação: %.2f litros\n", mean(insumos_laranja)))
    if (length(insumos_laranja) > 1) {
      cat(sprintf("Desvio Padrão: %.2f litros\n", sd(insumos_laranja)))
    } else {
      cat("Desvio Padrão: N/A (Requer mais de 1 fazenda cadastrada)\n")
    }
  } else {
    cat("\n-> Nenhuma fazenda de Laranja cadastrada.\n")
  }
  
} else {
  cat("\n[!] ERRO: Arquivo 'dados_farmtech.csv' não encontrado.\n")
}
cat("\n===================================================\n")