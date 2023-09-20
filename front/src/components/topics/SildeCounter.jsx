import React from 'react';
import '../../assets/css/topic/TopicSlide.css';

function SlideCounter({ slideNumber, total }) {
  return (
    <div className="SlideCounter">
      <p className="text-muted">
        {slideNumber}
        {' '}
        of
        {' '}
        {total}
      </p>
    </div>

  );
}

export default SlideCounter;
