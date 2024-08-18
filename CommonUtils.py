import psutil
import hashlib


class CommonUtils:
    """
    This class is for creating the common methods to execute test cases
    """

    def __init__(self):
        """
        This method is for initializing the common variables
        """
        self.processes = []

    def get_process_info(self):
        """
        This method is for getting the running process details using task manager
        :return: Running processes.
        """
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                process_info = f"{proc.info['pid']} {proc.info['name']} {proc.info['username']}"
                self.processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return self.processes

    @classmethod
    def generate_hash_value(cls, process_info):
        """
        This method is for generating the hash value using process name
        :param process_info: Provide process name to generate hash value
        :return: Hash ID
        """
        hash_object = hashlib.sha256(process_info.encode())
        return hash_object.hexdigest()
