import _plotly_utils.basevalidators


class CoastlinewidthValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='coastlinewidth', parent_name='layout.geo', **kwargs
    ):
        super(CoastlinewidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            min=0,
            role='style',
            **kwargs
        )