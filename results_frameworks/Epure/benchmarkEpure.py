from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Epure-elements',
                  predictions_file_or_folder='EPURE_process_elements.json',
                  output_results='results-epure-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Epure-elements-sharp',
                  predictions_file_or_folder='EPURE_process_elements.json',
                  output_results='results-epure-elements-sharp',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Epure-relations',
                  predictions_file_or_folder='EPURE_process_relations.json',
                  output_results='results-epure-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Epure-relations-sharp',
                  predictions_file_or_folder='EPURE_process_relations.json',
                  output_results='results-epure-relations-sharp',
                  relax_window=0)
