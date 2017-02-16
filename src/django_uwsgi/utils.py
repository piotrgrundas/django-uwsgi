import six


def dict_to_env_vars(input_dict):
    for key, value in six.iteritems(input_dict):
        if value is None:
            continue
        if isinstance(value, six.string_types):
            pass
        elif value is True:
            value = 'true'
        elif value is False:
            value = 'false'
        elif isinstance(value, six.integer_types):
            value = six.text_type(value)
        else:
            raise TypeError('Unknown option type: {} ({})'.format(
                key, type(value))
            )
        yield 'UWSGI_{}'.format(key.upper().replace('-', '_')), value
