---
title: M&E가 좋은 사업은 성과도 좋은가: 세계은행 사업평가 5,079건 다시 보기
date: 2026-10-12
summary: 세계은행 독립평가국(IEG) 사업평가 5,079건을 직접 계산해, M&E 품질과 성과 등급이 함께 움직이는 정도와 그 연관을 그대로 효과로 읽으면 안 되는 이유를 살펴봅니다.
tags: [M&E, 성과지표, 평가, 공개 데이터]
author: kardis
status: published
ai: yes
---

M&E 품질이 높은 사업은 성과 등급도 높을까요? 세계은행 독립평가국(IEG)이 공개한 사업평가 자료에서 M&E 등급과 성과 등급이 함께 매겨진 5,079건을 직접 계산해 보니, 둘은 매우 강하게 함께 움직였습니다. M&E가 「미흡(Negligible)」인 사업은 29.2%만 성과가 「보통 만족 이상」이었고, 「상당(Substantial)」인 사업은 94.3%였습니다. 다만 이 차이를 그대로 M&E의 효과로 읽어서는 안 됩니다. 차이의 상당 부분은 준비·감독 품질과 겹치고, 성과 등급 자체가 「입증된 증거」를 바탕으로 매겨지기 때문입니다. 이 자료가 가장 확실하게 말하는 것은 「M&E가 약한 사업은 성과를 인정받기 어렵다」는 점입니다.

## 무엇을 계산했는가

IEG World Bank Project Performance Ratings(2026-10-08 기준, 12,622행)를 내려받았습니다. 이 가운데 M&E 품질 등급이 있는 평가는 5,090건(평가연도 2007년 이후)입니다. 여기서 성과 등급이 「Not Rated」인 11건을 뺀 5,079건(사업 5,078개, 1개 사업은 평가 2건)을 분석했습니다. 성과는 6단계 등급 중 「보통 만족(Moderately Satisfactory)」 이상을 성공으로 묶었습니다.

| M&E 품질 | 평가 수 | 성과 보통 만족 이상 | 비율 |
|---|---|---|---|
| 미흡(Negligible) | 486 | 142 | 29.2% |
| 보통(Modest) | 2,397 | 1,637 | 68.3% |
| 상당(Substantial) | 2,058 | 1,940 | 94.3% |
| 높음(High) | 138 | 137 | 99.3% |
| 전체 | 5,079 | 3,856 | 75.9% |

![그림 1. M&E 품질 등급별 성과 「보통 만족 이상」 비율](https://raw.githubusercontent.com/kardisceo-kr/kardis-data/main/posts/img/2026-10-me-quality-outcome/fig1.png)

평가 방식을 나눠 봐도 모양은 같습니다. 문서 검토 방식인 ICRR(4,613건)에서는 미흡 28.1%, 상당 94.3%였습니다. IEG가 현장을 방문해 자료를 따로 모으는 PPAR(466건)에서도 미흡 35.0%, 상당 93.5%였습니다.

## 준비·감독 품질로 나눠 보면

M&E가 좋은 사업은 대개 준비와 감독도 좋습니다. 그래서 준비 품질(Quality at Entry)과 감독 품질(Quality of Supervision)을 같은 수준으로 맞춘 사업끼리 다시 비교했습니다.

| 비교 집단 | 미흡 | 보통 | 상당 | 높음 | 미흡↔상당 차이 |
|---|---|---|---|---|---|
| 전체(5,079건) | 29.2% | 68.3% | 94.3% | 99.3% | 65.0%p |
| 준비·감독 모두 보통 만족 이상(3,389건) | 82.3% (96건) | 88.8% | 97.0% | 99.3% | 14.7%p |
| 준비 품질 보통 불만족 이하(1,479건) | 14.5% | 41.9% | 67.6% | (2건) | 53.1%p |

![그림 2. 준비·감독 품질을 맞추면 M&E 등급 간 격차가 줄어든다](https://raw.githubusercontent.com/kardisceo-kr/kardis-data/main/posts/img/2026-10-me-quality-outcome/fig2.png)

준비와 감독이 모두 양호한 사업만 보면 미흡과 상당의 차이는 65.0%p에서 14.7%p로 줄어듭니다. 반대로 준비가 부실한 사업(감독 품질은 맞추지 않음)에서는 M&E 등급에 따른 차이가 53.1%p로 여전히 큽니다. 준비와 감독이 모두 부실한 628건만 보면 미흡 7.9%, 상당 29.6%(27건)로 차이는 21.7%p입니다.

준비 품질, 감독 품질, 지역, 평가 시기를 함께 넣은 로지스틱 회귀(5,056건)에서도 M&E 「상당」 사업이 「미흡」 사업보다 성과가 보통 만족 이상일 오즈가 약 8.6배(95% 신뢰구간 6.1~12.2)로 남았습니다. 같은 5,056건에서 통제하기 전의 40.6배보다는 크게 줄어든 값입니다.

## 다른 해석: 효과인가, 측정인가

![그림 3. M&E 등급과 성과 등급이 함께 움직이는 네 가지 경로](https://raw.githubusercontent.com/kardisceo-kr/kardis-data/main/posts/img/2026-10-me-quality-outcome/fig3.png)

첫째, 측정 효과입니다. IEG의 ICR 검토 지침은 효과성(Efficacy) 등급을 낮추는 경우로 「성과가 부족한 증거」뿐 아니라 「성과에 대한 증거가 부족한 경우」를 함께 듭니다. M&E가 약하면 실제 성과와 관계없이 성과를 입증하지 못해 등급이 낮아질 수 있습니다. IEG 연구자 Raimondo(2016)도 성과 등급이 「나쁜 결과」와 「결과를 입증할 증거 부족」이라는 서로 다른 현상을 섞을 수 있다고 지적했습니다.

둘째, 같은 평가자 문제입니다. ICRR에서는 한 사업의 M&E와 성과 등급을 같은 IEG 검토자가 같은 문서를 보고 매깁니다. Raimondo(2016)도 한 명의 검토자가 여러 항목을 사후에 평가하는 데서 오는 평가자 효과를 한계로 들었습니다. 두 점수가 서로 독립된 측정이 아니므로 연관이 실제보다 크게 보일 수 있습니다.

셋째, 보이지 않는 공통 원인입니다. Denizer·Kaufmann·Kraay(2013)는 6,000건이 넘는 세계은행 사업을 분석해, 성과 차이가 국가 사이보다 국가 안에서 훨씬 크고 사업 관리자의 역량 지표가 성과와 유의하게 관련된다고 보고했습니다. 유능한 관리자가 M&E도 잘 챙기고 사업도 잘 이끈다면, 이 자료의 연관은 관리자 역량을 반영한 것일 수 있습니다.

그렇다고 M&E의 효과가 없다는 뜻은 아닙니다. Raimondo(2016)는 2008~2014년에 평가된 투자사업 약 1,300건에 성향점수 매칭을 적용해, M&E가 좋은 사업의 IEG 성과 등급이 6점 척도에서 0.33~0.40점 높다고 추정했습니다(매칭 방식에 따라 다름). 같은 사업 관리자가 맡은 사업끼리 비교해도 M&E가 좋은 사업이 더 나은 성과 등급을 받을 오즈가 85% 높았습니다. 단순 비교보다 작지만 연관은 남는다는 결과입니다. 다만 이 연구도 관찰된 변수만 맞췄고 같은 IEG 등급을 결과로 썼기 때문에, 원저자도 인과 효과가 아닌 「연관」으로 표현했습니다.

## 시기별 변화

M&E가 미흡·보통인 사업의 비중은 평가연도 2007~2014년 69.2%(1,746건 중)에서 2015~2019년 61.1%, 2020년 이후 40.4%(1,742건 중)로 줄었습니다. 등급 분포가 위로 이동한 것이 실제 M&E 개선인지, 평가 기준 운용의 변화인지는 이 자료만으로 구분할 수 없습니다.

![그림 4. 평가 시기별 M&E 등급 구성](https://raw.githubusercontent.com/kardisceo-kr/kardis-data/main/posts/img/2026-10-me-quality-outcome/fig4.png)

## 한계

- 모든 등급은 IEG 평가자의 판단이며, 수혜자 수준의 성과를 직접 측정한 값이 아닙니다.
- 분석 대상은 M&E 등급이 매겨진 2007년 이후 평가 사업이고, 투자사업(IPF)이 86%를 차지합니다. 세계은행과 사업 구조가 다른 KOICA·EDCF 사업에 결과를 그대로 옮길 수 없습니다.
- 회귀분석은 관찰된 변수만 통제했으므로 인과 효과의 추정치가 아닙니다.

## 시사점

| 단계 | 확인하거나 바꿀 일 |
|---|---|
| 기획 | 성과지표마다 「종료평가 때 무엇을 증거로 내놓을지」를 PDM에 함께 적습니다. 이 자료에서 M&E가 「미흡」한 사업은 29.2%만 보통 만족 이상을 받았고, IEG 지침은 증거가 부족하면 효과성 등급을 낮추도록 합니다. |
| 착수 | 기초선 조사와 자료 수집 주기를 착수 단계에서 확정합니다. 준비 품질이 보통 불만족 이하인 사업에서는 M&E 등급에 따른 성과 차이가 53.1%p로, 준비·감독이 모두 양호한 사업(14.7%p)보다 컸습니다. |
| 집행 | 중간 점검 때 M&E 체계를 설계·실행·활용 세 측면으로 따로 확인합니다. IEG도 ICR 검토 지침에서 이 세 측면(Design·Implementation·Utilization)으로 M&E 품질을 봅니다. |
| 종료 | 성과 등급이 낮게 나왔다면 「성과 부족」인지 「증거 부족」인지 먼저 구분해 보고합니다. 두 경우의 교훈은 다릅니다. |

## 계산 방법

- 자료: IEG World Bank Project Performance Ratings 전체 CSV(2026-10-12 내려받음), 12,622행, 자료 기준일 2026-10-08.
- 필터: M&E Quality가 Negligible·Modest·Substantial·High인 행(5,090행) 중 Outcome이 6단계 등급인 행(Not Rated 제외) → 5,079행. 평가연도 2007~2027. 사업 ID P122764는 평가 2건(2023, 2026)이 모두 원자료에 있어 그대로 두었습니다.
- 성공 정의: Outcome이 Moderately Satisfactory, Satisfactory, Highly Satisfactory 중 하나.
- 층화: Quality at Entry와 Quality of Supervision을 각각 「보통 만족 이상」과 「보통 불만족 이하」로 나누고, Not Rated는 해당 층에서 뺐습니다. 표의 「준비 품질 보통 불만족 이하」 행은 감독 품질로 나누지 않았습니다.
- 시기: Evaluation FY 2007~2014, 2015~2019, 2020~2027.
- 회귀: 로지스틱 회귀. 종속변수는 성공(0/1), 설명변수는 M&E 등급(미흡 기준), 준비·감독 품질(각 2구분), 세계은행 지역(9개 범주), 평가 시기(3구간). 준비·감독 등급이 모두 있는 5,056건. 오즈비는 보통 2.56(1.93~3.40), 상당 8.62(6.11~12.17), 높음 46.9(6.4~344.1)이고, 통제 전에는 5.36, 40.6, 339입니다.
- 그림은 위 계산값으로 kardis가 직접 그렸습니다(Python).

## 출처

- [IEG World Bank Project Performance Ratings (DS00053)](https://financesone.worldbank.org/ieg-world-bank-project-performance-ratings/DS00053) · World Bank Independent Evaluation Group, World Bank Finances One, CC BY 4.0, 자료 기준일 2026-10-08
- [What Difference Does Good Monitoring & Evaluation Make to World Bank Project Performance?](https://documents1.worldbank.org/curated/en/180811468197076970/text/WPS7726.txt) · Estelle Raimondo, World Bank Policy Research Working Paper 7726, 2016
- [Guidelines for Reviewing World Bank Implementation Completion and Results Reports: A Manual for IEG ICR Reviewers](https://ieg.worldbankgroup.org/node/4077) · World Bank IEG, 2017-07-25 갱신(초안)
- [Good Countries or Good Projects? Macro and Micro Correlates of World Bank Project Performance](https://openknowledge.worldbank.org/entities/publication/06b521e6-7d1e-532a-9851-5e6c991bd568/full) · Cevdet Denizer, Daniel Kaufmann, Aart Kraay, Journal of Development Economics, 2013
- [What can we learn from the Independent Evaluation Group's project ratings and lessons?](https://ieg.worldbankgroup.org/node/57108) · Mari Noelle Roquiz, IEG, 2024-06-25
