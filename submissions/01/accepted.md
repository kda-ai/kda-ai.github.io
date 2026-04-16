 
# Submission list

## [214] Selin Coban, David Kierdorf, Cagatay Akpinar and Horst Lichter. CellFlow: A Tool For Automatic Jupyter Notebook Workflow Visualization.
### Abstract
Jupyter Notebooks are widely used in machine learning (ML) and data science, yet their linear, cell-based representation makes it difficult for developers to quickly form accurate mental models, especially when notebooks contain branching logic or alternative solution paths.
This paper presents CellFlow, a JupyterLab extension that automatically generates workflow diagrams from notebooks. CellFlow statically analyzes code cells using abstract syntax trees to identify variable definition–use dependencies and combines this analysis with LLM–generated semantic labels and descriptions. The resulting diagrams, named cell-flow diagrams, explicitly visualize computational activities and the flow of data artifacts between them, providing an architectural view of notebook workflows.
As a demonstration, we show how CellFlow integrates with JupyterLab and supports notebook comprehension. Initial user study results indicate that the generated diagrams help developers understand previously unseen notebooks more quickly and are perceived as useful and easy to use.


## [307] Gopal Shendge, Lisha Ahuja, Chandan Prakash, Pavan Kumar Chittimalli and Ravindra Naik. An Efficient Approach for Model Recovery from Image Containing Diagrams.
### Abstract
Driven by the need to meet dynamic business demands and keep pace with technological advancements, modernizing legacy systems is a critical aspect of enterprise IT evolution. A key challenge during this transition is extracting meaningful insights from diagrammatic and visual representations, which play a vital role in existing systems. These visual models provide deep insights into system components, data flows, and interdependencies, which are essential for understanding the structure and behavior of legacy systems. However, extracting relevant information from these visual representations remains a significant challenge, since existing tools lack the ability to identify complex parts of the diagrams, resulting in incomplete, coarse‑grained model recovery. This paper presents a novel approach for the extraction of entity‑relationship schemas from legacy data models. We propose a combined method leveraging large language models (LLMs) and object detection techniques to improve accuracy in identifying entities and relationships. Our approach achieves 98% precision for entity recovery and 61% relation‑existence accuracy over the evaluated candidate‑pair set. We discuss the challenges encountered during the process of model recovery and outline potential solutions to further improve the robustness and scalability of the approach.

## [321] Tim Lukas Adam, Phongsakon Mark Konrad, Riccardo Terrenzi, Florian Girardo Lukas, Rahime Yilmaz, Krzysztof Sierszecki and Serkan Ayvaz. CAKE: Cloud Architecture Knowledge Evaluation of Large Language Models.
### Abstract
In today’s software architecture, large language
models (LLMs) serve as software architecture co-pilots. However,
no benchmark currently exists to evaluate large language mod-
els’ actual understanding of cloud-native software architecture.
For this reason we present a benchmark called CAKE, which
consists of 188 expert-validated questions covering four cognitive
levels of Bloom’s revised taxonomy—recall, analyze, design, and
implement—and five cloud-native topics. Evaluation is conducted
on 22 model configurations (0.5B–70B parameters) across four
LLM families, using three-run majority voting for multiple-
choice questions (MCQs) and LLM-as-a-judge scoring for free
responses. Based on this evaluation, four notable findings were
identified. First, MCQ accuracy plateaus above 3B parameters,
with the best model reaching 99.2%. Second, free-response
scores scale steadily across all cognitive levels. Third, the two
formats capture different facets of knowledge, as the MCQ
accuracy approaches a ceiling while free-responses continue to
differentiate models. Finally, reasoning augmentation (+think)
improves free-response quality, while tool augmentation (+tool)
degrades performance for small models. These results suggest
that the evaluation format fundamentally shapes how we measure
architectural knowledge in LLMs.


## [322] Abdullah Huzeyfe Köse, Rahime Yılmaz and Feza Buzluca. An Empirical Analysis of LLM-Driven Refactoring for Microservices.
### Abstract
Large Language Models (LLMs) are increasingly used in software engineering, raising the question of whether they can reliably support refactoring in microservice‑based systems, where architectural constraints and deployment requirements make refactoring particularly complex. This study empirically examines LLM‑driven refactoring using a structured, three‑phase prompting protocol applied twice to four microservices previously labeled as low‑maintainability by experienced developers. Three state‑of‑the‑art LLMs, GPT‑5.2 Extended Thinking, Claude Opus 4.5, and Gemini 3 Pro, were evaluated across analysis, refactoring, and self‑audit phases, followed by deployment, execution, and metric‑based validation. Of 24 total refactorings, 22 successfully passed build and run verification, showing that LLM‑supported refactoring is feasible in real microservice environments. Across all models, refactored microservices demonstrated consistent improvements in software quality. Maximum cognitive complexity decreased by about 45%, maximum cyclomatic complexity by around 31%, and average cognitive complexity by 26%, while code duplication decreased by roughly 9%. Expectedly, LOC and NoM increased due to the enforced method‑decomposition strategy. Model behaviors varied: Claude Opus 4.5 produced the strongest overall reductions in complexity, and Gemini 3 Pro achieved competitive improvements with the smallest code growth. Overall, the findings indicate that LLM‑driven, developer‑assisted refactoring can produce measurable and functionally safe improvements in microservice‑based systems.