from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Declarative-elements',
                  predictions_file_or_folder='Declarative_elements.json',
                  output_results='results-declarative-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Declarative-elements-sharp',
                  predictions_file_or_folder='Declarative_elements.json',
                  output_results='results-declarative-elements-sharp',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Declarative-relations',
                  predictions_file_or_folder='Declarative_relations.json',
                  output_results='results-declarative-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Declarative-relations-sharp',
                  predictions_file_or_folder='Declarative_relations.json',
                  output_results='results-declarative-relations-sharp',
                  relax_window=0)
