import abc 

class Executor(metaclass=abc.ABCMeta):
    ''' Subject '''
    @abc.abstractmethod 
    def run(self, cmd):
        pass 


class ConcreteExecutor(Executor):
    ''' Real subject '''
    def run(self, cmd):
        print(f"{cmd} command executed")


class ExecutorProxy(Executor):

    def switch_role(self, user, pwd):
        self.is_admin = False 
        # never ever add the passwords to your source code
        if user == "Admin" and "abc123" == pwd:
            self.is_admin = True 

    def __init__(self, user, pwd):
        '''
        self.is_admin = False 
        # never ever add the passwords to your source code
        if user == "Admin" and "abc123" == pwd:
            self.is_admin = True
        '''
        self.switch_role(user, pwd) 
        
        self.executor = ConcreteExecutor()

    def run(self, cmd):
        if self.is_admin:
            self.executor.run(cmd)
        else: 
            if cmd.strip().startswith("rm"):
                raise Exception("rm command is not allowed for non-admin users.")
            else:
                self.executor.run(cmd)

def main():

    executor: Executor = ExecutorProxy("Admin", "123123123")
    try:
        executor.run("ls -l")
        executor.run("rm -rf /")
    
    except Exception as e:
        print(e)
    
    # The role has been switched to the admin 
    executor.switch_role('Admin', 'abc123')
    
    try:
        executor.run("rm -rf /")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
        


