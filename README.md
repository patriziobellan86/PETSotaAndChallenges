This is the repository of the paper:

# Process Extraction from Text: Benchmarking the State of the Art and Paving the Way for Future Challenges

**Abstract** 
*The extraction of process models from text refers to the problem of turning the information contained in an unstructured textual process descriptions into a formal representation, i.e., a process model. 
Several automated approaches have been proposed to tackle this problem, but they are highly heterogeneous in scope (what they exactly do) and underlying assumptions, such as differences in input, target output, and data used in their evaluation. As a result, it is currently unclear how well existing solutions are able to solve the model-extraction problem and how they compare to each other.
In this paper, we overcome this issue by comparing 10 state-of-the-art approaches for model extraction in a systematic manner, covering both qualitative and quantitative aspects.
The qualitative evaluation compares the analysis of the primary studies on:
- the main characteristics of each solution; 
- the type of process elements extracted from the input data; and	
- the experimental evaluation performed to evaluate the proposed framework.

The results show a heterogeneity of techniques, elements extracted and evaluations conducted, that are often impossible to compare in a direct manner. To overcome this difficulty we propose a quantitative comparison of the tools proposed by the different papers on the unifying task of process model entity and relation extraction so as to be able to compare them directly. The results show three distinct groups of tools in terms of performance, with no tool obtaining very good scores and also serious limitations in terms of elements extracted. Moreover, the proposed evaluation pipeline can be considered a reference task on a well defined dataset and metrics that can be used to compare new tools in a way similar to what happens in e.g., the natural language processing or computer vision communities. 
The paper also presents a reflection on the results of the qualitative and quantitative evaluation on the limitations and challenges that the community needs to address in the future to produce significant advances in this area.*


**Keywords**
- Process Model Extraction from Text, 
- Process Discovery,
- Business Process Management,
- Process Model,
- Natural Language Processing


## Tools Tested:

- de A. R. **Gonçalves**, J. C., Santoro, F. M., & Baião, F. A. (2011).
Let Me Tell You a Story - On How to Build Process Models.
J. UCS, 17, 276–295. doi:10.3217/ jucs-017-02-0276

- **van der Aa**, H., Di Ciccio, C., Leopold, H., & Reijers, H. A. (2019). Extracting
declarative process models from natural language. In Advanced Information
Systems Engineering - 31st International Conference, CAiSE 2019, Proceedings
980 (pp. 365–382). Springer volume 11483 of Lecture Notes in Computer Science.
doi:10.1007/978-3-030-21290-2\_23.

- **Friedrich**, F., Mendling, J., & Puhlmann, F. (2011). Process Model Generation from
Natural Language Text. In Advanced Information Systems Engineering - 23rd International Conference, CAiSE 2011. Proceedings (pp. 482–496). Springer volume
6741 of Lecture Notes in Computer Science.

- **Epure**, E. V., Martín-Rodilla, P., Hug, C., Deneckère, R., & Salinesi, C. (2015).
Automatic process model discovery from textual methodologies.
In 9th IEEE International Conference on Research Challenges in Information Science,
RCIS 2015 (pp.19–30). IEEE. doi:10.1109/RCIS.2015.7128860.

- **Honkisz**, K., Kluza, K., & Wisniewski, P. (2018). A Concept for Generating Business
Process Models from Natural Language Description. In Knowledge Science, Engineering
and Management - 11th International Conference, KSEM 2018, Proceedings, Part I (pp. 91–103). Springer volume 11061 of Lecture Notes in Computer
Science. doi:10.1007/978-3-319-99365-2\_8.

- **Qian**, C., Wen, L., Kumar, A., Lin, L., Lin, L., Zong, Z., Li, S., & Wang, J. (2020).
An approach for process model extraction by multi-grained text classification. In
Advanced Information Systems Engineering - 32nd Int. Conference, CAiSE 2020,
Proceedings (pp. 268–282). Springer volume 12127 of Lecture Notes in Computer
Science. doi:10.1007/978-3-030-49435-3\_17.

## The results of the benchmarking

The folder *Approaches* contains the results of the benchmarking procedure for each tool tested.
In the tool folder you can find the following files:
- bankmarking{AUTHOR_NAME}.py: the python script file to run the benchmarking procedure
- {AUTHOR_NAME}_process_elements.json: the file containing the process elements extracted by the tool
- {AUTHOR_NAME}_process_relations.json: the file containing the process relations extracted by the tool
- results-{AUTHOR_NAME}-{elements/relations} {type of comparison}.json: the file containing the results of the benchmarking procedure. 
Type of comparison can be *strict* or empty in the relaxed setting.
For example the file 'results-Goncalves-elements-strict.json' contains the results of the benchmarking procedure for the tool of Goncalves in the strict setting for the process elements.
- info.txt: the file containing the information about the tool tested


## Benchmarking

To (re)-run benchmarking procedure of a tool you need to run the corresponding python script file *benchmark{AUTHOR_NAME}.py*.
You can find the script file in the folder of the tool tested.

To do so, you need to install **petbenchmarks** python package.
This package contains the benchmarking procedure.
You can install it via pip:

```python
pip install petbenchmarks
```

