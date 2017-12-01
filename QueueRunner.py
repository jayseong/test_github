import tensorflow as tf

tf.set_random_seed(777)  # for reproducibility

num_epochs = 10

filenames = [("data_%02d.csv" % i) for i in range(1, 6)]

filename_queue = tf.train.string_input_producer(
    ['data_01.csv', 'data_02.csv', 'data_03.csv', 'data_04.csv', 'data_05.csv'],
    num_epochs=num_epochs, shuffle=True, name='filename_queue')

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)


# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
record_defaults = [[0.], [0.], [0.], [0.]]
xy = tf.decode_csv(value, record_defaults=record_defaults)

# collect batches of csv in
train_x_batch, train_y_batch = \
    tf.train.batch([xy[0:-1], xy[-1:]], batch_size=10)


# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# print('key   : ', sess.run(key))
# print('value : ', sess.run(value))

# Start populating the filename queue.
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for epoch in range(num_epochs):
    x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
    print('step : ----------------------', step)
    print(x_batch)

coord.request_stop()
coord.join(threads)



