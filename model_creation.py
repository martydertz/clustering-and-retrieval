

topic_model = gl.load_model('lda_assignment_topic_model')
tpm_low_gamma = gl.load_model('lda_low_gamma')
tpm_high_gamma = gl.load_model('lda_high_gamma')

topics = topic_model.get_topics(num_words=1500)
topics_low_gamma = tpm_low_gamma.get_topics(num_words = 1500)
topics_high_gamma = tpm_high_gamma.get_topics(num_words = 1500)


topics.export_csv(filename = "topics_base_model.csv")
topics_low_gamma.export_csv(filename = "topics_low_gamma_model.csv")
topics_high_gamma.export_csv(filename = "topics_high_gamma_model.csv")
