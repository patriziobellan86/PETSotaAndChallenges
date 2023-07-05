from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Epure-elements',
                  predictions_file_or_folder='EPURE_process_elements.json',
                  output_results='results-epure-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Epure-elements-strict',
                  predictions_file_or_folder='EPURE_process_elements.json',
                  output_results='results-epure-elements-strict',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Epure-relations',
                  predictions_file_or_folder='EPURE_process_relations.json',
                  output_results='results-epure-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Epure-relations-strict',
                  predictions_file_or_folder='EPURE_process_relations.json',
                  output_results='results-epure-relations-strict',
                  relax_window=0)
