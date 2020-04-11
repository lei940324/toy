#include "MainWindow.h"
#include "ui_MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_action_triggered()
{

}

void MainWindow::on_action_2_triggered()
{
    
}

void MainWindow::on_lineEdit_1_cursorPositionChanged(int arg1, int arg2)
{
    
}

void MainWindow::on_action_3_triggered()
{

}

void MainWindow::on_action_4_triggered()
{

}
