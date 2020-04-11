from tkinter import *
from tkinter.messagebox import showinfo
from svm_handler import SVMHandler
import time
from mail import sendemail


def run_gui():
    prediction_time = 0
    training_time = 0
    results = ""
    root = Tk()
    root.title("SVM GUI - Amit Nimrodi")
    # Here you need to set the frame, grid, row and column configurations of the root.
    root.geometry('425x250')
    #Head title
    head_lbl = Label(root,text="Welcome to Amit Nimrodi's SVM app",font=("Arial Bold",16))
    #Secondary title - project explanation
    project_explanation_lbl = Label(root,text="Using LinearSVC, this model is trained using data with over 32,000\n"
                                          "instances, each instance is characterized with 14 different features,\n"
                                          "in order to predict whether the instance is more likely to earn less\n"
                                          "or over 50k a year"
                                ,font=("Arial",10))
    head_lbl.grid(column=0,row=0)
    project_explanation_lbl.grid(column=0,row=1)
    svm_handler = SVMHandler()

    # Here you need to start the training of the svm. Remember, the other actions (testing/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def activate_train():
        start_train = time.time()
        svm_handler.train()
        global training_time
        training_time = time.time() - start_train
        showinfo('Training done','Training time took: {} seconds\n\n'
                                 'Out of {} instaces, {} were valid and used'
                 .format(training_time, svm_handler.get_train_data_size(), svm_handler.get_valid_train_data_size()))
        # Here you need to start the testing with the svm. Remember, the other actions (training/sending mail) must be
        # responsive to users actions (i.e. hitting their button)- How can this be achieved?

    def activate_test():
        try:
            start_prediction = time.time()
            svm_handler.predict()
            global prediction_time
            prediction_time = time.time() - start_prediction
            global results
            results=svm_handler.measure_accuracy()
            showinfo('Results of prediction',
                     'Error percentage is: {}%\nPrediction time took: {} seconds\n\n'
                     'Out of {} instances in test data, {} were valid and used'
                     .format(results, prediction_time, svm_handler.get_test_data_size(),
                             svm_handler.get_valid_test_data_size()))
        #Warn the user: 'predict' button should be clicked after 'train' button is clicked.
        except AttributeError:
            showinfo('Error','You have to train the model before predicting')

    # Here you need to send an email with the svm testing result. Remember, the other actions (training/testing)
    # must be responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def send_mail():
        global results
        global training_time
        global prediction_time
        try:
            message_body = 'Error percentage is: {}%\n' \
                           'Training time took: {} seconds\n' \
                           'Prediction time took: {} seconds\n' \
                           'Total time took: {}\n' \
                           '\n'\
                           'Out of {} instances in train data, {} were valid and used'\
                           'Out of {} instances in test data, {} were valid and used'\
                .format(results, training_time, prediction_time, training_time+prediction_time,
                        svm_handler.get_train_data_size(),svm_handler.get_valid_train_data_size(),
                        svm_handler.get_test_data_size(),svm_handler.get_valid_test_data_size())
            try:
                sendemail(message_body)
                showinfo('Sent email successfully', 'The email body that was sent is: \n\n%s' %message_body )
            finally:
                pass
        except (AttributeError, NameError):
            showinfo('Error','You have to train the model & predict before sending mail')

    train_btn = Button(root,text="Start training",bg="blue",fg="white",command=activate_train)
    predict_btn = Button(root,text="Predict",bg="blue",fg="white",command=activate_test)
    send_mail_btn = Button(root,text="Send results through mail",bg="blue",fg="white",command=send_mail)
    train_btn.grid(column=0,row=2)
    predict_btn.grid(column=0,row=3)
    send_mail_btn.grid(column=0,row=4)
    root.mainloop()


if __name__ == "__main__":
    run_gui()