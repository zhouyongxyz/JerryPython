class View:

    # @params string name view file
    # @params array data
    def render(self, obj, view, data=None):
        """

        :rtype: object
        """
        if data is None:
            result = getattr(obj, view)()
        else:
            result = getattr(obj, view)(data)
        return result
