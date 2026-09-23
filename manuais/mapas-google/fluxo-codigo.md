# fluxo-codigo.md — #51 Mapas do Google (uso interno, NÃO publicar)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `mapas-google.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

- Menu **Aplicativos** → Entrega → **Mapas Google** (`app.id === 'mapas-google'`).
- `GoogleMapsModal` (lista) + `GoogleMapsConfigModal` (campo `googleMapsKey`).
- Ao salvar com chave preenchida, o produto pode abrir `GoogleMapsApiValidatorPanel`.
- Hook `useGoogleMapsConfig`.

