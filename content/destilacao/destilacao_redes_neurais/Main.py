import torch
from Device import device
from DataLoader import train_loader, test_loader
from Models import DeepNN, LightNN
from Train import train
from Test import test
from KnowledgeDistill import train_knowledge_distillation

# Seed for reproducibility
torch.manual_seed(42)

# Instantiate and train the teacher model
teacher_model = DeepNN(num_classes=10).to(device)
train(teacher_model, train_loader, epochs=10, learning_rate=0.001, device=device)
test_accuracy_teacher = test(teacher_model, test_loader, device)

# Instantiate the student model
student_model = LightNN(num_classes=10).to(device)
test_accuracy_student_without_kd = test(student_model, test_loader, device)

# Print model parameters
print(f"DeepNN parameters: {sum(p.numel() for p in teacher_model.parameters()):,}")
print(f"LightNN parameters: {sum(p.numel() for p in student_model.parameters()):,}")

# Train the student model with knowledge distillation
new_student_model = LightNN(num_classes=10).to(device)
train_knowledge_distillation(
    teacher=teacher_model, student=new_student_model, train_loader=train_loader, 
    epochs=10, learning_rate=0.001, T=2, soft_target_loss_weight=0.25, ce_loss_weight=0.75, device=device
)

# Evaluate student model
test_accuracy_student_kd = test(new_student_model, test_loader, device)

# Print final accuracies
print(f"Teacher accuracy: {test_accuracy_teacher:.2f}%")
print(f"Student accuracy without train: {test_accuracy_student_without_kd:.2f}%")
print(f"Student accuracy with KD: {test_accuracy_student_kd:.2f}%")
