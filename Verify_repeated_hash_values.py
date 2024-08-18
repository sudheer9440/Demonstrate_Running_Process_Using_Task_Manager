from CommonUtils import CommonUtils


class VerifyRepeatedHASHValues:
    """
    This class is for verifying repeated hash values in single run
    """
    def __init__(self):
        """
        This method is for initializing the requied variables
        """
        self.process_count = {}

    def validate_hash_values(self):
        """
        This method is for validating the repeated hash values
        :return: None
        """
        processes = CommonUtils().get_process_info()
        for process in processes:
            hash_value = CommonUtils().generate_hash_value(process_info=process.split(' ')[1])
            if hash_value in self.process_count:
                self.process_count[hash_value] += 1
            else:
                self.process_count[hash_value] = 1
            print(f"Process Info: {process.split(' ')[1]}, {self.process_count[hash_value]}")


if __name__ == "__main__":
    VerifyRepeatedHASHValues().validate_hash_values()
