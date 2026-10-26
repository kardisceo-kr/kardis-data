---
title: 설문 문항과 번역 점검을 AI에 맡길 때: 결함 12개를 심은 가상 설문으로 비교한 직접 대조와 역번역
date: 2026-10-26
summary: 결함 12개를 심은 가상 기초선 설문(영어 원문과 스페인어 번역본)을 AI에 두 방식으로 각 3회 점검시켜, 원문과 번역본을 직접 대조하는 방식과 역번역을 거치는 방식의 차이, 그리고 설문 점검에서 AI에 맡길 일과 사람이 판단할 일을 정리합니다.
tags: [AI 활용, 설문, 번역, 기초선 조사]
author: kardis
status: published
ai: yes
---

설문 문항 검토와 번역 점검에서 AI에 맡길 일과 맡기지 말 일은 무엇일까요? 결론부터 말씀드리면, 원문과 번역본을 나란히 주고 문장 단위로 대조하게 하는 일(회상 기간, 단위, 척도 방향, 빠진 구절)과 문항 설계 결함의 1차 점검은 AI에 맡길 만합니다. 반면 AI에게 역번역을 시켜 원문과 비교하는 방식은 단계가 하나 늘고, 이번 시험에서는 그 단계에서 거짓 경보가 생겼습니다. 유럽사회조사(ESS) 지침도 역번역보다 팀 검토 방식을 택하고 있어, 역번역을 단독 점검 수단으로 쓰지 않기를 권합니다. 응답자가 실제로 문항을 어떻게 알아듣는지, 어떤 지적을 받아들일지는 사람이 사전시험과 판정으로 정해야 합니다.

## 직접 해 본 시험: 결함 12개를 심은 가상 설문

kardis는 이 판단을 시험으로 확인했습니다. 가상 농촌 생계 사업의 기초선 가구 설문 10문항을 영어 원문(기준본)과 현장용 스페인어 번역본으로 만들고, 결함 12개를 일부러 심었습니다. 원문 설계 결함 6개(품질·가격 이중질문, 「기타」 없는 보기, 유도형 부정 의문, 회상 기간 없음, 겹치는 소득 구간, 전문용어)와 번역 결함 6개(7일이 30일로 바뀜, 만족도 척도 방향 뒤집힘, 「주된」 누락, 「5세 미만 포함」 누락, kg이 파운드로 바뀜, 쉬운 말을 어려운 문어체로 옮김)입니다. 한 문항(Q10)은 결함 없는 대조 문항으로 두었습니다.

두 경로를 3회씩 실행했습니다. 직접 대조 경로는 AI 한 번에 원문과 번역본을 함께 주었습니다. 역번역 경로는 한 AI가 원문을 모른 채 스페인어를 영어로 역번역하고, 다른 AI가 원문과 역번역을 비교하게 했습니다.

![그림 1. 결함별 검출 결과(실행 6회)](https://raw.githubusercontent.com/kardisceo-kr/kardis-data/main/posts/img/2026-10-ai-survey-translation/fig1.png)

| 결함 | 직접 대조(3회) | 역번역 경로(3회) |
|---|---|---|
| 원문 설계 결함 6개 | 18/18 | 해당 없음(원문 설계는 대조 대상이 아님) |
| 번역 결함 6개 | 18/18 | 18/18 |
| 합계 | 36/36 | 18/18 |

표 1. 경로별 검출 수(kardis 시험).

직접 대조는 3회 모두 12개를 찾았습니다. 3회 모두 30일로 바뀐 기간이 응답 범위 「0–7일」과 맞지 않는다는 점, kg이 파운드로 바뀌면 보고서 수치가 약 2.2배 어긋난다는 점까지 짚었습니다. 한 실행은 「pernoctó」(밤을 보냈다)가 「배고픈 채 잠자리에 들었다」와 뜻이 다르다는 점도 지적했습니다. 역번역 경로도 번역 결함 6개는 3회 모두 찾았습니다. 이번 시험에서는 역번역이 번역 결함을 가리지 않았습니다.

## 차이가 난 곳: 원문의 모호함이 번역 오류로 둔갑하다

![그림 2. 실행별 지적 구성](https://raw.githubusercontent.com/kardisceo-kr/kardis-data/main/posts/img/2026-10-ai-survey-translation/fig2.png)

| 실행 | 심은 결함 검출 | 심지 않은 추가 지적 | 그중 원문 그대로인 번역을 번역 오류로 본 지적 | 합계 |
|---|---|---|---|---|
| 직접1 | 12 | 4 | 0 | 16 |
| 직접2 | 12 | 3 | 0 | 15 |
| 직접3 | 12 | 3 | 0 | 15 |
| 역번역1 | 6 | 2 | 1 | 8 |
| 역번역2 | 6 | 4 | 1 | 10 |
| 역번역3 | 6 | 2 | 1 | 8 |

표 2. 실행별 지적 수(kardis 시험). 스스로 철회한 지적은 뺐습니다.

차이는 Q4에서 나왔습니다. 스페인어 번역본의 「¿No está de acuerdo…?」는 원문 「Don't you agree…?」의 모호한 부정 의문을 그대로 옮긴 것입니다. 역번역 3회는 모두 이 문장을 「Do you disagree…?」 쪽으로 읽어 옮겼고, 대조 3회는 모두 이를 번역 오류로 본 목록에 올렸습니다(「결과가 반전될 수 있음」, 「예/아니오의 의미가 뒤집힘」). 원문의 모호함이 번역 오류로 둔갑해, 원문 그대로인 번역을 고치라는 지적이 된 것입니다. 직접 대조도 2회는 P4를 지적했지만, 「설계 결함이 번역본에서도 그대로 남았다」고 원인을 원문에 돌렸으므로 거짓으로 세지 않았습니다.

같은 입력을 3회 돌려도 이 지적은 줄지 않았습니다. 역번역 결과가 3회 거의 같았기 때문입니다. 이번 시험에서 반복 실행은 같은 방향으로 되풀이되는 오류를 걸러내지 못했습니다.

![그림 3. 두 경로의 흐름과 거짓 경보가 생긴 단계](https://raw.githubusercontent.com/kardisceo-kr/kardis-data/main/posts/img/2026-10-ai-survey-translation/fig3.png)

| 경로 | 입력 | AI 호출 | 볼 수 있는 결함 | 거짓 번역 오류 지적 |
|---|---|---|---|---|
| 직접 대조 | 원문+번역본 | 1회 | 설계·번역 | 매회 0건 |
| 역번역 경유 | 번역본 → 역번역 → 원문과 대조 | 2회 | 번역만 | 매회 1건(Q4) |

표 3. 두 경로 비교(kardis 시험).

## 방법론과 선행 연구가 말하는 것

설문 번역 방법론도 같은 방향을 가리킵니다. Walde와 Völlm(2023)은 TRAPD(번역·검토·판정·사전시험·기록)를 설명하며, 역번역 과정에서도 번역 실수가 생길 수 있고 원문에 지나치게 붙은 번역을 낳을 수 있다는 지적을 인용합니다. 이들의 사전시험에서는 어떤 번역자도 짚지 못한 문제가 응답자 면담에서 드러났습니다. 유럽사회조사(ESS) 11차 번역 지침은 자신들의 팀 번역 방식이 역번역보다 질적으로 낫다고 밝히고, 나라마다 현장조사 전에 사전시험을 하도록 요구합니다. 다만 세계보건기구(WHO)의 WHODAS 2.0 번역 지침은 번역자가 문제로 표시한 항목을 원문을 보지 않은 독립 언어전문가가 역번역하고, 전문가 패널이 차이를 정리해 최종 번역을 정하게 합니다. 역번역을 버리기보다 패널 판정과 함께 쓰는 보조 절차로 둔 것으로 읽을 수 있습니다.

AI 검토의 성능에 대한 연구도 주의를 줍니다. 에식스대 사회경제연구소(ISER)의 2026년 작업논문은 결함을 심은 20문항으로 AI 사전검토를 시험해, 가장 좋은 설정에서 알려진 문제의 75%를 찾았고 거짓 양성은 적었다고 보고했습니다. 다만 결과는 지시문과 모델에 따라 달랐고, 검출률이 높았던 공개 가중치 모델은 결함 문항과 잘 만든 문항을 잘 가려내지 못했습니다. 예테보리대 연구진(Metheney·Yehle)은 ChatGPT(GPT-3.5·GPT-4)에 대상 언어 지정 여부를 바꾼 여섯 조건에서 문항 282개의 번역 난점을 짚게 했습니다. 미리 넣어 둔 문제 중 일부 유형은 여섯 조건 모두에서 찾았지만, 문제 두 개를 넣은 한 문항은 어느 조건에서도 정확히 찾아내지 못했습니다. 저자들은 출력의 정확성은 평가하지 못했고, 온라인 자료가 적은 언어에는 결과가 그대로 적용되지 않을 수 있다고 밝혔습니다.

## 맡길 일, 맡기지 말 일, 확인하는 방법

- 맡길 일: 원문과 번역본의 문장 단위 대조(숫자, 기간, 단위, 척도 방향, 빠지거나 더해진 구절), 이중질문·보기 누락·구간 겹침 같은 설계 결함의 1차 점검, 어려운 표현의 쉬운 말 대안 제시.
- 맡기지 말 일: 응답자가 문항을 어떻게 알아듣는지에 대한 판단(사전시험), 현지 단위와 지역 어휘의 선택, 지적의 최종 채택(판정), AI 역번역만으로 번역 품질을 판정하는 일.
- 확인 방법: 결함을 심은 시험 설문으로 먼저 검출 수준을 잽니다. 「번역 오류」 지적은 반드시 번역본 원문에서 그 차이가 실제로 있는지 확인합니다. 남은 판단은 응답자 인지면담으로 확인합니다.

![그림 4. TRAPD 단계별 AI 역할](https://raw.githubusercontent.com/kardisceo-kr/kardis-data/main/posts/img/2026-10-ai-survey-translation/fig4.png)

| 단계 | 이번 글의 정리 |
|---|---|
| T 번역 | 번역가 초안(이번 시험 범위 밖) |
| R 검토 | AI 직접 대조로 1차 지적 목록(맡길 일) |
| A 판정 | 사람이 지적 채택 여부 결정(맡기지 말 일) |
| P 사전시험 | 사람이 응답자 인지면담(맡기지 말 일) |
| D 기록 | AI를 쓴 단계와 확인 내역을 남김 |

표 4. TRAPD 단계별 AI 역할(Walde·Völlm(2023)이 소개한 단계에 이번 시험 결과를 대응).

## 다른 해석과 한계

역번역 경로도 번역 결함을 모두 찾았으니, 대상 언어를 모르는 담당자에게는 여전히 유용하다고 볼 수 있습니다. 실제로 이번 거짓 경보는 원문 Q4가 부정 의문문이라는 설계 결함에서 비롯됐습니다. 원문을 먼저 고쳤다면 생기지 않았을 수 있습니다. 그러나 현장 설문에는 이런 모호한 문장이 늘 섞여 있고, 역번역은 그 모호함을 오류로 바꿔 보여 줄 수 있습니다. 대상 언어를 모른다면 역번역 결과의 지적을 원어민 검토자에게 확인받는 단계를 함께 두어야 합니다.

이 글의 한계도 밝힙니다. 시험은 설문 1건, 언어 1쌍(영어–스페인어), 모델 1종, 경로별 3회입니다. 결함은 kardis가 알아보기 쉽게 만들었고, 검출 판정도 kardis가 했으므로 판정자 편향이 있을 수 있습니다. 스페인어는 자료가 많은 언어여서, 자료가 적은 현지어에서는 결과가 다를 수 있습니다. 실제 응답자를 만나지 않았으므로 문항이 현장에서 통하는지는 확인하지 않았습니다. 이 결과는 AI 사용이 설문 품질을 높인다는 인과를 보여 주지 않습니다.

## 시사점

| 단계 | 확인하거나 바꿀 일 |
|---|---|
| 기획 | 설문 번역 계획에 「AI 직접 대조 → 사람 판정 → 응답자 사전시험」 순서를 적고, AI 역번역만으로 번역 품질을 판정하지 않는다고 명시합니다. |
| 착수 | 기초선 설문을 AI로 점검하기 전에 결함을 심은 시험 설문 1건으로 검출 수준을 재고 기록합니다. 대상 언어나 모델을 바꾸면 다시 잽니다. |
| 착수·집행 | AI가 「번역 오류」로 지적한 항목은 번역본 원문에서 차이가 실제로 있는지 원어민 검토자가 확인한 뒤에만 고칩니다. 부정 의문문처럼 모호한 원문은 번역 전에 먼저 고치고, 현장 조사 중 문항을 고칠 때도 같은 확인을 거칩니다. |
| 종료 | 평가 대비 문서에 설문 번역의 어느 단계에서 AI를 썼고 무엇을 사람이 확인했는지 남깁니다. |

## 계산 방법

- 대상: kardis가 만든 가상 설문 1건(배경 메모 4줄, 영어 원문 10문항, 스페인어 번역본 10문항). 실제 사업·기관 자료는 쓰지 않았습니다.
- 심은 결함 12개. 설계: Q2 품질·가격 이중질문, Q3 보기에 「기타」·빗물·구입한 물 없음, Q4 「Don't you agree…」 유도형 부정 의문, Q5 회상 기간 없음, Q6 소득 구간 경계 겹침(500, 1,000, 2,000), Q8 「climate-smart agriculture」 전문용어. 번역: P1 「past 7 days」→「últimos 30 días」, P2 척도 1=매우 불만족→1=매우 만족으로 역전, P3 「main source」 누락, P5 「including children under 5」 누락, P7 「kilograms」→「libras」, P9 「go to sleep at night hungry」→「pernoctó en estado de privación alimentaria」.
- 방법: 범용 AI 모델(Claude Sonnet 계열)을 서로 독립된 새 세션으로 호출했습니다. 직접 대조는 배경 메모·원문·번역본을 한 번에 주고 설계와 번역의 문제를 모두 찾게 했습니다(3회). 역번역 경로는 원문을 모르는 세션이 스페인어를 영어로 직역에 가깝게 역번역하고(3회), 다른 세션이 배경 메모·원문·역번역을 보고 번역에서 의미가 달라졌을 곳만 찾게 했습니다(3회). 정답표는 주지 않았고 도구 사용은 금지했습니다.
- 판정 기준: 본 목록이나 확신 낮음 목록에서 해당 결함을 문항 번호와 함께 지적하면 검출로 셌습니다. 「원문 그대로인 번역을 번역 오류로 본 지적」은 번역본이 원문을 그대로 옮겼는데도 번역 오류로 지적한 경우입니다(kardis 판정). 원문 결함이 번역본에 그대로 남았다고 밝힌 지적은 여기에 세지 않았습니다.
- 그림은 위 집계값으로 kardis가 직접 그렸습니다(Python).

시험에 쓴 영어 원문과 스페인어 번역본은 다음과 같습니다(가상).

| 번호 | 영어 원문(기준본) | 스페인어 번역본(현장용) |
|---|---|---|
| 1 | In the past 7 days, how many days did your household eat meat or fish? (0–7 days) | En los últimos 30 días, ¿cuántos días comió carne o pescado su hogar? (0–7 días) |
| 2 | How satisfied are you with the quality and price of water from the community tap? 1=Very dissatisfied … 5=Very satisfied | ¿Qué tan satisfecho está con la calidad y el precio del agua del grifo comunitario? 1=Muy satisfecho … 5=Muy insatisfecho |
| 3 | What is the main source of drinking water for your household? 1=Piped water, 2=Protected well, 3=River or stream | ¿De dónde obtiene su hogar el agua para beber? 1=Agua entubada, 2=Pozo protegido, 3=Río o arroyo |
| 4 | Don't you agree that the new irrigation canal has improved your harvest? 1=Yes, 2=No | ¿No está de acuerdo en que el nuevo canal de riego ha mejorado su cosecha? 1=Sí, 2=No |
| 5 | How many times did any household member, including children under 5, visit a health centre? | ¿Cuántas veces algún miembro de su hogar visitó un centro de salud? |
| 6 | What was your household's total cash income last month? 1=0–500 pesos, 2=500–1,000 pesos, 3=1,000–2,000 pesos, 4=More than 2,000 pesos | ¿Cuál fue el ingreso total en efectivo de su hogar el mes pasado? 1=0–500 pesos, 2=500–1.000 pesos, 3=1.000–2.000 pesos, 4=Más de 2.000 pesos |
| 7 | How much maize did your household harvest in the last main season? (in kilograms) | ¿Cuánto maíz cosechó su hogar en la última temporada principal? (en libras) |
| 8 | Has your household adopted climate-smart agriculture practices? 1=Yes, 2=No | ¿Su hogar ha adoptado prácticas de agricultura climáticamente inteligente? 1=Sí, 2=No |
| 9 | In the past 4 weeks, did anyone in your household go to sleep at night hungry because there was not enough food? 1=Yes, 2=No | En las últimas 4 semanas, ¿algún integrante de su hogar pernoctó en estado de privación alimentaria por insuficiencia de alimentos? 1=Sí, 2=No |
| 10 | Who in your household usually decides how to spend money from crop sales? 1=Myself, 2=My spouse, 3=Myself and my spouse jointly, 4=Someone else | ¿Quién en su hogar decide normalmente cómo gastar el dinero de la venta de cosechas? 1=Yo, 2=Mi cónyuge, 3=Yo y mi cónyuge juntos, 4=Otra persona |

## 출처

- [The TRAPD approach as a method for questionnaire translation](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2023.1199989/pdf) · P. Walde, B. A. Völlm, Frontiers in Psychiatry 14:1199989, 2023-06-15
- [ESS Round 11 Translation Guidelines](https://europeansocialsurvey.org/sites/default/files/2024-08/ESS_R11_Translation_Guidelines.pdf) · ESS ERIC(GESIS 작성), 2022-09-12
- [WHODAS 2.0 Translation Package (Version 1.0)](https://terrance.who.int/mediacentre/data/WHODAS/Guidelines/WHODAS%202.0%20Translation%20guidelines.pdf) · 세계보건기구(WHO), 발행일 미표기
- [LLMs for survey pretesting: how well can large language models identify flaws in survey questions?](https://www.iser.essex.ac.uk/?p=233381) · University of Essex ISER, Survey Futures Working Paper No. 15, 2026-04-15
- [Exploring the Potential Role of Generative AI in the TRAPD Procedure for Survey Translation](https://arxiv.org/pdf/2411.14472) · E. A. Metheney, L. Yehle(University of Gothenburg), arXiv:2411.14472, 2024
