## code生成任务 eval 方案

#### 1. 信息汇总

https://github.com/ryan-gz/code_gen_eval

| 测试集        | 类型   | 数据量                            | 描述                                                         | url                                                          |
| ------------- | ------ | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| CodeSearchNet | multi  | over 2 million                    | 10余种代码。用于代码表示学习的数据集、工具和基准。           | https://github.com/github/CodeSearchNet?tab=readme-ov-file#evaluation |
| DS-1000       | python | total:1000                        | 纯python任务，聚焦 pandas/pytorch/Scipy/Sklean/Tensorflow/Matplotlib 包的代码生成 | https://github.com/xlang-ai/DS-1000                          |
| MBPP          | python | total:1000                        | 由大约 1,000 个 Python 编程问题组成，旨在由入门级程序员解决，涵盖编程基础知识、标准库功能等。 每个问题都包含任务描述、代码解决方案和 3 个自动化测试用例。 | https://github.com/google-research/google-research/tree/master/mbpp |
| ODEX          | python | total: 439                        | 开放域代码生成的基于执行的评估                               | https://github.com/zorazrw/odex                              |
| CoNaLa        | python | train:2379, test:500              | 该挑战旨在测试“从自然语言生成程序片段”的系统。               | https://conala-corpus.github.io                              |
| CoNaLa-Ext    | python | total:11422                       | CoNaLa的扩充                                                 | https://github.com/gabeorlanski/stackoverflow-encourages-cheating |
| APPS          | python | train:5000, test:5000             | APPS 数据集由从不同开放访问编码网站（例如 Codeforces、Kattis 等）收集的问题组成。 APPS 基准测试试图反映如何通过以不受限制的自然语言提出编码问题并评估解决方案的正确性来评估人类程序员。 问题的难度从入门到大学竞赛级别不等，衡量编码能力以及解决问题的能力。 | https://github.com/hendrycks/apps                            |
| Turbulence    | python | total:60                          | Turbulence 是一个新的基准，用于系统地评估用于代码生成的指令调整大型语言模型 (LLM) 的正确性和鲁棒性。 Turbulence 由大量自然语言问题模板组成，每个模板都是一个编程问题，经过参数化，以便可以以多种不同的形式提出问题。 | https://github.com/ShahinHonarvar/Turbulence-Benchmark       |
| WikiSQL       | sql    | train:56355, test:15878, dev:8421 | 用于开发自然语言界面的大型带注释语义解析语料库。             | https://github.com/salesforce/WikiSQL                        |
| BIRD          | sql    | total:12751                       | BIRD（BIg Bench for Large-scale Database Grounded Text-to-SQLvaluation）代表了一个开创性的跨域数据集，它检查了广泛的数据库内容对 文本到 SQL 的解析。 BIRD 包含超过 12,751 个独特的问题 SQL 对、95个大型数据库，总大小为 33.4 GB。 | https://bird-bench.github.io                                 |
| SPIDER        | sql    | total:10181                       | Spider是一个大型的语义解析和文本到 SQL 数据集。 Spider 挑战的目标是开发跨域数据库的自然语言接口。 它由 10,181 个问题和 5,693 个独特的复杂 SQL 查询组成，涉及 200 个数据库以及覆盖 138 个不同领域的多个表。 | https://yale-lily.github.io/spider                           |
| SParC         | sql    | total:4298                        | SParC 是 Spider 任务的上下文相关/多回合版本，是一个复杂且跨域的 text- SQL 挑战。 SParC 由 4,298 个连贯的问题序列组成（12k 多个独特的个人问题，由 14 名耶鲁大学学生注释的 SQL 查询注释），这些问题序列是从用户与 138 个领域的 200 个复杂数据库的交互中获得的。 | https://yale-lily.github.io/sparc                            |
| CoSQL         | sql    | total:10000                       | CoSQL 是一个用于构建跨域 text2sql系统的语料库。 它是 Spider和 SParC任务。 CoSQL 由 30k+ 轮和 10k+ 带注释的 SQL 查询组成，这些查询是从 [Wizard-of-Oz] 获得的 | https://yale-lily.github.io/cosql                            |

#### 2. 借鉴方案

##### 2.1. DeepSeek-Coder

![image-20240517141056257](https://raw.githubusercontent.com/ryan-gz/img_cache/main/uPic/image-20240517141056257.png)

##### 2.2. Starcoder

```markdown
6 Evaluation
In this section, we first outline the models we evaluated in addition to StarCoder and StarCoderBase. Then we report on the Python language performance of all models on the HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), and DS-1000 (Lai et al., 2022) evaluation benchmarks. Then we cover multi-language evaluation using a variety of benchmarks and tasks.
```

##### 2.3. CodeXGLUE

```
5.6 Text-to-code generation
Setting. We use the CONCODE dataset for text-to-code generation. Models are expected to generate source codes of Java class member functions, given natural language descriptions and class environments. We report the exact match accuracy, the BLEU score [56], and the CodeBLEU score [65]. We use the CodeBLEU score as the overall evaluation metric.
Results. Table 10 presents the results on the CONCODE test set. Seq2Seq [70] is an RNN-based sequence to sequence model. Seq2Action + MAML [26] combines a context-aware retrieval model with model-agnostic meta-learning (MAML). Iyer-Simp
+ 200 idoms [36] extracts code idioms and applies idioms-based decoding. We also report the performance of pretrained models, in- cluding GPT-2 [59], CodeGPT, and CodeGPT-adapted. CodeGPT- adapted achieves the CodeBLEU score of 35.98, resulting in a state- of-the-art performance.
```

![image-20240517114133681](https://raw.githubusercontent.com/ryan-gz/img_cache/main/uPic/image-20240517114133681.png)

##### 2.4. CodeT5

```
4.3 Downstream Tasks and Metrics
We cover most generation and understanding tasks in the CodeXGLUE benchmark (Lu et al., 2021) and employ the provided public datasets and the same data splits following it for all these tasks.
... Code generation is the task to gen- erate a code snippet based on NL descriptions. We employ the Concode data (Iyer et al., 2018) in Java where the input contains both NL texts and class environment contexts, and the output is a function. We evaluate it with BLEU-4, exact match (EM) accuracy, and CodeBLEU (Ren et al., 2020) that considers syntactic and semantic matches based on the code structure in addition to the n-gram match.
```

##### 2.5. CodeLlama

```markdown
3 Results
We report results on a variety of benchmarks. 
First, we evaluate our models on popular description-to-code generation benchmarks for Python: HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), and APPS(programming interviews and competitions, Hendrycks et al., 2021).
Second, we evaluate our models on further programming languages using MultiPL-E (Cassano et al., 2023), namely on C++, Java, PHP, C#, TypeScript (TS), and Bash. We additionally report results on the GSM8K benchmark (Cobbe et al., 2021), which measures mathematical reasoning capabilities (Appendix D).
```

#### 3. 具体细节

##### 3.1. CODE GEN BENCHMARK

1. DS-1000(Data Science 1000)

   https://github.com/xlang-ai/DS-1000

   python code task, pandas/pytorch/Scipy/Sklean/Tensorflow/Matplotlib

   Official data and code release for the paper "DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation"

2. MBPP:   Mostly Basic Python Problems Dataset

   https://github.com/google-research/google-research/tree/master/mbpp

   The benchmark consists of around 1,000 crowd-sourced Python programming problems, designed to be solvable by entry level programmers, covering programming fundamentals, standard library functionality, and so on. Each problem consists of a task description, code solution and 3 automated test cases.


2. CoNaLa: The Code/Natural Language Challenge

   https://conala-corpus.github.io

   This challenge was designed to test systems for *generating program snippets from natural language*. For example, if the input is `sort list x in reverse order`, then the system would be required to output `x.sort(reverse=True)` in Python.

3. APPS (Automated Programming Progress Standard)

   https://github.com/hendrycks/apps

   https://people.eecs.berkeley.edu/~hendrycks/APPS.tar.gz

   The APPS dataset consists of problems collected from different open-access coding websites such as Codeforces, Kattis, and more. The APPS benchmark attempts to mirror how humans programmers are evaluated by posing coding problems in unrestricted natural language and evaluating the correctness of solutions. The problems range in difficulty from introductory to collegiate competition level and measure coding ability as well as problem-solving.

4. Code Generation on Django

   https://github.com/odashi/ase15-django-dataset

   The **Django** dataset is a dataset for code generation comprising of 16000 training, 1000 development and 1805 test annotations. Each data point consists of a line of Python code together with a manually created natural language description.

5. CoNaLa-Ext (CoNaLa Extended With Question Text)

   https://github.com/gabeorlanski/stackoverflow-encourages-cheating

   The **CoNaLa Extended With Question Text** is an extension to the original [CoNaLa Dataset](https://conala-corpus.github.io/) ([Papers With Code Link](https://paperswithcode.com/dataset/conala)) proposed in the NLP4Prog workshop paper "[Reading StackOverflow Encourages Cheating: Adding Question Text Improves Extractive Code Generation](https://arxiv.org/abs/2106.04447)". The key additions are that every example now has the full question body from its respective StackOverflow Question.

6. Turbulence Benchmark

   https://github.com/ShahinHonarvar/Turbulence-Benchmark

   Turbulence is a new benchmark for systematically evaluating the correctness and robustness of instruction-tuned large language models (LLMs) for code generation. Turbulence consists of a large set of natural language question templates, each of which is a programming problem, parameterised so that it can be asked in many different forms. Each question template has an associated test oracle that judges whether a code solution returned by an LLM is correct. Thus, from a single question template, it is possible to ask an LLM a neighbourhood of very similar programming questions, and assess the correctness of the result returned for each question. This new benchmark systematically and automatically identifies cases where LLMs are able to solve some problems in a neighbourhood but do not manage to generalise to solve the whole neighbourhood. Therefore, this method is effective at highlighting robustness issues. The corresponding paper is available at https://arxiv.org/abs/2312.14856.

##### 3.2. SQL BENCHMARK 

1. WikiSQL

   https://huggingface.co/datasets/wikisql

   A large crowd-sourced dataset for developing natural language interfaces for relational databases.

   WikiSQL is a dataset of 80654 hand-annotated examples of questions and SQL queries distributed across 24241 tables from Wikipedia.

2. **BIRD（benchmark）**

   https://bird-bench.github.io

   BIRD (**BI**g Bench for La**R**ge-scale **D**atabase Grounded Text-to-SQL Evaluation) represents a pioneering, cross-domain dataset that examines the impact of extensive database contents on text-to-SQL parsing. BIRD contains over **12,751**unique question-SQL pairs, **95** big databases with a total size of **33.4 GB**.

3. **SPIDER（benchmark）**

   https://yale-lily.github.io/spider

   SPIDER 2.0 原定24年3月更新上线，目前还没有找到

   Spider is a large-scale [*complex and cross-domain*](https://medium.com/@tao.yu/spider-one-more-step-towards-natural-language-interfaces-to-databases-62298dc6df3c) semantic parsing and text-to-SQL dataset annotated by 11 Yale students. The goal of the Spider challenge is to develop natural language interfaces to cross-domain databases. It consists of 10,181 questions and 5,693 unique complex SQL queries on 200 databases with multiple tables covering 138 different domains. In Spider 1.0, different complex SQL queries and databases appear in train and test sets. To do well on it, systems must *generalize well to not only new SQL queries but also new database schemas*.

4. SParC

   https://yale-lily.github.io/sparc

   ***SParC\*** is a dataset for cross-domain **S**emantic **Par**sing in **C**ontext. It is the context-dependent/multi-turn version of the [***Spider task\***](https://yale-lily.github.io/spider), a complex and cross-domain text-to-SQL challenge. SParC consists of 4,298 coherent question sequences (12k+ unique individual questions annotated with SQL queries annotated by 14 Yale students), obtained from user interactions with 200 complex databases over 138 domains.

5. CoSQL

   https://yale-lily.github.io/cosql

   ***CoSQL*** is a corpus for building cross-domain **Co**nversational text-to-**SQL** systems. It is the dialogue version of the [***Spider\***](https://yale-lily.github.io/spider)and [***SParC\***](https://yale-lily.github.io/sparc) tasks. CoSQL consists of 30k+ turns plus 10k+ annotated SQL queries, obtained from a [Wizard-of-Oz](https://en.wikipedia.org/wiki/Wizard_of_Oz_experiment)collection of 3k dialogues querying 200 complex databases spanning 138 domains. Each dialogue simulates a real-world DB query scenario with a crowd worker as a user exploring the database and a SQL expert retrieving answers with SQL, clarifying ambiguous questions, or otherwise informing of unanswerable questions.

##### 3.3. TABLE QA BENCHMARK

1. Compositional Semantic Parsing on Semi-Structured Tables

   https://ppasupat.github.io/WikiTableQuestions/

   Answer complex questions on semi-structured tables using question-answer pairs as supervision.

2. TabFact

   https://tabfact.github.io

   A large-scale dataset with 16k Wikipedia tables as evidence for 118k human annotated statements to study fact verification with semi-structured evidence

3. [MultiModalQA](https://arxiv.org/abs/2104.06039)

   https://allenai.github.io/multimodalqa/

   MultiModalQA is a challenging question answering dataset that requires joint reasoning over text, tables and images, consisting of [29,918](https://github.com/allenai/MultiModalQA) examples.







