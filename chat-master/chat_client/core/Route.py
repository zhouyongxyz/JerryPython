
class Route:

    @staticmethod
    def go(obj, path, data=None):
        """

        :rtype: object
        """
        if data is None:
            result = getattr(obj, path)()
        else:
            result = getattr(obj, path)(data)
        return result
