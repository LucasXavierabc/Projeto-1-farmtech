
#################### Valores dos insumos das plantações exemplo

mudas_laranja <- c(333, 366, 403, 333, 480)
agua_laranja <- c(150000, 165000, 181500, 150000, 216000)
nitrogenio_laranja <- c(80000, 88000, 96800, 80000, 115200)
fosforo_laranja <- c(40000, 44000, 48400, 40000, 57600)
potassio_laranja <- c(60000, 66000, 72600, 60000, 86400)

sementes_milho <- c(23000, 25300, 27830, 23000, 33120)
agua_milho <- c(50000, 55000, 60500, 50000, 72000)
nitrogenio_milho <- c(100000, 110000, 121000, 100000, 144000)
fosforo_milho <- c(50000, 55000, 60500, 50000, 72000)
potassio_milho <- c(80000, 88000, 96800, 80000, 115200)



#################### Insumos de laranja junto de milho
mudas_sementes_todas <- c(mudas_laranja, sementes_milho)
agua_todas <- c(agua_laranja, agua_milho)
nitrogenio_todas <- c(nitrogenio_laranja, nitrogenio_milho)
fosforo_todas <- c(fosforo_laranja, fosforo_milho)
potassio_todas <- c(potassio_laranja, potassio_milho)



#################### Função para calcular média, moda e mediana

library(DescTools)
calcular_dados <- function(vetor){
  return(
    list(
      media = mean(vetor),
      mediana = median(vetor),
      moda = Mode(vetor)
    )
  )
}



#################### Lista com todos os dados juntos
estatisticas <- list(
  dados_mudas_laranja = calcular_dados(mudas_laranja),
  dados_agua_laranja = calcular_dados(agua_laranja),
  dados_nitrogenio_laranja = calcular_dados(nitrogenio_laranja),
  dados_fosforo_laranja = calcular_dados(fosforo_laranja),
  dados_potassio_laranja = calcular_dados(potassio_laranja),
  dados_sementes_milho = calcular_dados(sementes_milho),
  dados_agua_milho = calcular_dados(agua_milho),
  dados_nitrogenio_milho = calcular_dados(nitrogenio_milho),
  dados_fosforo_milho = calcular_dados(fosforo_milho),
  dados_potassio_milho = calcular_dados(potassio_milho),
  dados_mudas_sementes_todas = calcular_dados(mudas_sementes_todas),
  dados_agua_todas = calcular_dados(agua_todas),
  dados_nitrogenio_todas = calcular_dados(nitrogenio_todas),
  dados_fosforo_todas = calcular_dados(fosforo_todas),
  dados_potassio_todas = calcular_dados(potassio_todas)
)



################### imprimir informações na tela

options(scipen = 999)  # Desativa notação científica
for (nome in names(estatisticas)) {
  cat("\n--- Estatísticas para", nome, "---\n")
  cat("Média:", format(estatisticas[[nome]]$media, big.mark = ".", decimal.mark = ","), "\n")
  cat("Mediana:", format(estatisticas[[nome]]$mediana, big.mark = ".", decimal.mark = ","), "\n")
  cat("Moda:", paste(format(estatisticas[[nome]]$moda, big.mark = ".", decimal.mark = ","), collapse=", "), "\n")
}












################### Usando a API publica Weather API para coletar dados da cidade de São Paulo, SP

library(httr)
library(jsonlite)

api_key <- "3301f72c9b9540609e932341252303"
cidade <- "São Paulo"
cidade_codificada <- URLencode(cidade)

url <- paste0("http://api.weatherapi.com/v1/current.json?key=", api_key, "&q=", cidade_codificada)
resposta <- GET(url)


if (status_code(resposta) == 200) {
  dados_meteorologicos <- fromJSON(content(resposta, "text"))

  temperatura <- dados_meteorologicos$current$temp_c
  umidade <- dados_meteorologicos$current$humidity
  condicao <- dados_meteorologicos$current$condition$text

  temp_laranja <- (temperatura >= 25 && temperatura <= 30)
  umid_laranja <- (umidade >= 60 && umidade <= 80)
  cond_laranja <- (condicao != "Rain" && condicao != "Heavy rain")

  temp_milho <- (temperatura >= 20 && temperatura <= 30)
  umid_milho <- (umidade >= 60 && umidade <= 80)
  cond_milho <- (condicao != "Rain" && condicao != "Heavy rain")



  ################## Imprimir condições meteorológicas na tela

  cat("Informações meteorológicas para", cidade, ":\n")
  cat("Temperatura:", temperatura, "°C\n")
  cat("Umidade:", umidade, "%\n")
  cat("Condição do tempo:", condicao, "\n")



  ################## Verificar se condições estão favoráveis para o cultivo de laranja/milho

  if (temp_laranja && umid_laranja && cond_laranja) {
    cat("As condições climáticas estão favoráveis para o cultivo de laranja.\n")
  } else {
    cat("As condições climáticas não estão favoráveis para o cultivo de laranja.\n")
  }

  if (temp_milho && umid_milho && cond_milho) {
    cat("As condições climáticas estã6 favoráveis para o cultivo de milho.\n")
  } else {
    cat("As condições climáticas não estão favoráveis para o cultivo de milho.\n")
  }

} else {
  cat("Erro ao acessar a API. Verifique a chave de API e a conexão.")
}
temp_milho <- (temperatura >= 20 && temperatura <= 30)
umid_milho <- (umidade >= 60 && umidade <= 80)
cond_milho <- (condicao != "Rain" && condicao != "Heavy rain")



################## Imprimir condições meteorológicas na tela

cat("Informações meteorológicas para", cidade, ":\n")
cat("Temperatura:", temperatura, "°C\n")
cat("Umidade:", umidade, "%\n")
cat("Condição do tempo:", condicao, "\n")



################## Verificar se condições estão favoráveis para o cultivo de laranja/milho

if (temp_laranja && umid_laranja && cond_laranja) {
  cat("As condições climáticas estão favoráveis para o cultivo de laranja.\n")
} else {
  cat("As condições climáticas não estão favoráveis para o cultivo de laranja.\n")
}

if (temp_milho && umid_milho && cond_milho) {
  cat("As condições climáticas estão favoráveis para o cultivo de milho.\n")
} else {
  cat("As condições climáticas não estão favoráveis para o cultivo de milho.\n")
}