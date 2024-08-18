import time

from CommonUtils import CommonUtils


class VerifyRepeatedHASHValuesFor1Min:
    """
    This class is for verifying repeated hash values in single run
    """
    def __init__(self):
        """
        This method is for initializing the requied variables
        """
        self.process_count = {}

    def validate_hash_values_for_1min(self):
        """
        This method is for validating the repeated hash values in task manager
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

    @classmethod
    def validate_hash_value_in_loop(cls):
        t_end = time.time() + 60
        while time.time() < t_end:
            VerifyRepeatedHASHValuesFor1Min().validate_hash_values_for_1min()


if __name__ == "__main__":
    VerifyRepeatedHASHValuesFor1Min.validate_hash_value_in_loop()
    while True:
        VerifyRepeatedHASHValuesFor1Min().process_count.clear()
        time.sleep(5)

