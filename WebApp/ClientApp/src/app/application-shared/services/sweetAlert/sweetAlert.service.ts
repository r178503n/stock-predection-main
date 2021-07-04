import { Injectable } from '@angular/core';
import Swal from 'sweetalert2';
// declare let Swal: any;

@Injectable({
  providedIn: 'root',
})
export class SweetAlertService {
  constructor() {}

  basic(message: any) {
    Swal.fire(message);
  }

  async emailInput() {
    const { value: email } = await Swal.fire({
      title: 'Input email address',
      input: 'email',
      inputPlaceholder: 'Enter your email address',
    });

    return email;
  }

  message(header: string, message: string) {
    Swal.fire({
      title: header,

      text: message,
      width: 600,
      padding: '3em',
      background: '#fff url(/images/trees.png)',
      backdrop: `
        rgba(0,0,123,0.4)
        url("/images/nyan-cat.gif")
        left top
        no-repeat
      `,
    });
  }

  success(message: string) {
    const Toast = Swal.mixin({
      toast: true,
      position: 'bottom-end',
      showConfirmButton: true,

      timer: 3000,
      timerProgressBar: true,
      onOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer);
        toast.addEventListener('mouseleave', Swal.resumeTimer);
      },
    });
    Toast.fire({
      icon: 'success',
      title: message,
      background: '#5CB811', //'#3085d6',
    });
  }

  success2(message: string) {
    Swal.fire({
      position: 'center',
      icon: 'success',
      title: message,
      showConfirmButton: false,
      timer: 1100,
    });
  }

  success3(message: string) {
    Swal.fire({
      icon: 'success',
      title: 'Done',
      text: message,
      // footer: '<a href>Why do I have this issue?</a>'
    });
  }

  error(message: string) {
    const Toast = Swal.mixin({
      toast: true,
      position: 'bottom-end',
      showConfirmButton: true,

      timer: 3000,
      timerProgressBar: true,
      onOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer);
        toast.addEventListener('mouseleave', Swal.resumeTimer);
      },
    });
    Toast.fire({
      icon: 'error',
      title: message,
      // background: '#5CB811', //'#3085d6',
    });
  }

  error2(message: string) {
    Swal.fire({
      position: 'center',
      icon: 'error',
      title: message,
      showConfirmButton: false,
      timer: 1100,
    });
  }

  error3(message: string) {
    Swal.fire({
      icon: 'error',
      title: 'Error Occured',
      text: message,
      footer: '<a href>Why do I have this issue?</a>',
    });
  }
  info(message: string) {
    Swal.fire({
      position: 'center',
      icon: 'info',
      title: message,
      showConfirmButton: false,
      timer: 1100,
    });
  }
  info2(message: string) {
    const Toast = Swal.mixin({
      toast: true,
      position: 'bottom-end',
      showConfirmButton: true,

      timer: 3000,
      timerProgressBar: true,
      onOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer);
        toast.addEventListener('mouseleave', Swal.resumeTimer);
      },
    });
    Toast.fire({
      icon: 'info',
      title: message,
      background: '#5CB811', //'#3085d6',
    });
  }
  confirm(confirmButtonText?, text?) {
    if (!text) {
      text = "You won't be able to revert this!";
    }
    if (!confirmButtonText) {
      confirmButtonText = 'Yes, cancel it!';
    }
    return Swal.fire({
      title: 'Are you sure?',
      text: text,
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: confirmButtonText,
    });
    /*
    .then(result => {
      if (result.value) {
        Swal.fire('Deleted!', 'Your file has been deleted.', 'success');
      }
    });*/

    /*
  Swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
    if (result.value) {
      Swal.fire(
        'Deleted!',
        'Your file has been deleted.',
        'success'
      )
    }
  });*/
  }
}
