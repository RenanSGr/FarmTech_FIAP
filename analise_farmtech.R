cat("\n[1] Processando dados das fazendas...\n")

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